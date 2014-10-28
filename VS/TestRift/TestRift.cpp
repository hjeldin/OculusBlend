// TestRift.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#pragma comment(lib,"RiftBlend.lib")
#include "RiftBlend.hpp"


int _tmain(int argc, _TCHAR* argv[])
{
	RiftBlend rf;
	rf.connect();
	while (1)
	{
		rf.pollSensors();
	}
	rf.disconnect();
	return 0;
}

