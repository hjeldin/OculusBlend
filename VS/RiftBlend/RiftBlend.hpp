#pragma once
#include "include/OVR.h"
#include "Include/OVR_CAPI_GL.h"
#include <iostream>
#include <vector>
class RiftBlend
{
public:
	RiftBlend();
	~RiftBlend();
	void connect();
	void disconnect();
	void pollSensors();
	std::vector<double>  headPose;

private:
	ovrHmd hmd;
};
