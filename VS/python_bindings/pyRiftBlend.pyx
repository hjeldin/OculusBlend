from libcpp.vector cimport vector

cdef extern from "RiftBlend.hpp":
    cdef cppclass RiftBlend:
        RiftBlend()

        vector[double] headPose

        void connect()
        void disconnect()
        void pollSensors()


cdef class PyRift:
    cdef RiftBlend* thisptr      # hold a C++ instance which we're wrapping
    def __cinit__(self):
        self.thisptr = new RiftBlend()
    def __dealloc__(self):
        del self.thisptr

    def pollSensor(self):
        self.thisptr.pollSensors()

    def connect(self):
        self.thisptr.connect()

    def disconnect(self):
        self.thisptr.disconnect()

    property headPose:
      def __get__(self): return self.thisptr.headPose
