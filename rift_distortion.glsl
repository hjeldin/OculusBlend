uniform sampler2D bgl_RenderedTexture;

const vec4 kappa = vec4(1.0,0.5,0,0.0);
const vec4 chromaParams = vec4(0.996f, -0.004f, 1.014, 0.0f);

uniform float screen_width;
uniform float screen_height;

const float scaleFactor = 0.9;

const vec2 leftCenter = vec2(0.25, 0.5);
const vec2 rightCenter = vec2(0.75, 0.5);

// Scales input texture coordinates for distortion.
vec2 hmdWarp(vec2 LensCenter, vec2 texCoord, vec2 Scale, vec2 ScaleIn) {
    vec2 theta = (texCoord - LensCenter) * ScaleIn; 
    float rSq = theta.x * theta.x + theta.y * theta.y;
    vec2 rvector = theta * (kappa.x + kappa.y * rSq + kappa.z * rSq * rSq + kappa.w * rSq * rSq * rSq);
    vec2 tc = LensCenter + Scale * rvector;
    return tc;
}

bool validate(vec2 tc, int left_eye) {
    //keep withlin bounds of texture 
    if ((left_eye == 1 && (tc.x < 0.0 || tc.x > 0.5)) ||   
        (left_eye == 0 && (tc.x < 0.5 || tc.x > 1.0)) ||
        tc.y < 0.0 || tc.y > 1.0) {
        return false;
    }
    return true;
}

void main() {
    vec2 screen = vec2(1920, 1080);

    float as = float(screen.x / 2.0) / float(screen.y);
    vec2 Scale = vec2(0.5, as);
    vec2 ScaleIn = vec2(2.0 * scaleFactor, 1.0 / as * scaleFactor);

    vec2 texCoord = gl_TexCoord[0].st;

    vec2 tc = vec2(0);
    vec4 color = vec4(0);
    
    if (texCoord.x < 0.5) {
        float green, blue, red;
        tc = hmdWarp(leftCenter, texCoord, Scale, ScaleIn );

        green = texture2D(bgl_RenderedTexture, tc).g;
        
        vec2  theta = (texCoord - leftCenter) * ScaleIn;
        float rSq = theta.x * theta.x + theta.y * theta.y;
        vec2 thetaColor = theta * (kappa.x + kappa.y * rSq + kappa.z * rSq * rSq + kappa.w * rSq * rSq * rSq);
        vec2 thetaBlue = thetaColor * (chromaParams.z + chromaParams.w * rSq);
        vec2 tcBlue = leftCenter + Scale * thetaBlue;
        vec2 thetaRed = thetaColor * (chromaParams.x + chromaParams.y * rSq);
        vec2 tcRed = leftCenter + Scale * thetaRed;
        blue = texture2D(bgl_RenderedTexture, tcBlue).b;
        red = texture2D(bgl_RenderedTexture, tcRed).r;
        
        color = vec4(red,green,blue,1);
        
        if (!validate(tc, 1))
            color = vec4(0);
    } else {
        float green, blue, red;
        tc = hmdWarp(rightCenter, texCoord, Scale, ScaleIn );
        
        green = texture2D(bgl_RenderedTexture, tc).g;
        
        vec2  theta = (texCoord - rightCenter) * ScaleIn;
        float rSq = theta.x * theta.x + theta.y * theta.y;
        vec2 thetaColor = theta * (kappa.x + kappa.y * rSq + kappa.z * rSq * rSq + kappa.w * rSq * rSq * rSq);
        vec2 thetaBlue = thetaColor * (chromaParams.z + chromaParams.w * rSq);
        vec2 tcBlue = rightCenter + Scale * thetaBlue;
        vec2 thetaRed = thetaColor * (chromaParams.x + chromaParams.y * rSq);
        vec2 tcRed = rightCenter + Scale * thetaRed;
        blue = texture2D(bgl_RenderedTexture, tcBlue).b;
        red = texture2D(bgl_RenderedTexture, tcRed).r;
        
        color = vec4(red,green,blue,1);
        if (!validate(tc, 0))
            color = vec4(0);
    }   
    
    color.a = 1;
    gl_FragColor = color;
}
