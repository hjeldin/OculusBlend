#include "RiftBlend.hpp"

RiftBlend::RiftBlend()
{
}


RiftBlend::~RiftBlend()
{
}

void RiftBlend::connect()
{
	ovr_Initialize();
	hmd = ovrHmd_Create(0);

	if (hmd != nullptr){

		std::cout << hmd->FirmwareMajor << " " << hmd->FirmwareMinor << std::endl;

		if (!ovrHmd_GetTrackingState(hmd, 0.0f).StatusFlags & ovrStatus_HmdConnected){
			std::cout << "could not connect" << std::endl;
		}

		unsigned int hmdCaps = ovrHmdCap_DynamicPrediction | ovrHmdCap_LowPersistence;

		ovrHmd_SetEnabledCaps(hmd, hmdCaps);

		unsigned sensorCaps = ovrTrackingCap_Orientation | ovrTrackingCap_MagYawCorrection;
		sensorCaps |= ovrTrackingCap_Position;

		ovrHmd_ConfigureTracking(hmd, sensorCaps, 0);

		for (auto i = 0; i < 7; i++)
			headPose.push_back(0);
	}
}



void RiftBlend::disconnect()
{
	if (hmd != nullptr){
		ovrHmd_Destroy(hmd);
		ovr_Shutdown();
	}
}

void RiftBlend::pollSensors()
{
	if (hmd != nullptr){
		ovrTrackingState ss = ovrHmd_GetTrackingState(hmd, ovr_GetTimeInSeconds());
		if (ss.StatusFlags & (ovrStatus_OrientationTracked | ovrStatus_PositionTracked))
		{
			headPose[0] = ss.HeadPose.ThePose.Position.x;
			headPose[1] = ss.HeadPose.ThePose.Position.y;
			headPose[2] = ss.HeadPose.ThePose.Position.z;
			headPose[3] = ss.HeadPose.ThePose.Orientation.x;
			headPose[4] = ss.HeadPose.ThePose.Orientation.y;
			headPose[5] = ss.HeadPose.ThePose.Orientation.z;
			headPose[6] = ss.HeadPose.ThePose.Orientation.w;
		}
	}

}
