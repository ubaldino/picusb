import usb.core
dev = usb.core.find()
print( dev.bDescriptorType )
"""
 |  Additionally, the class provides methods to communicate with
 |  the hardware. Typically, an application will first call the
 |  set_configuration() method to put the device in a known configured
 |  state, optionally call the set_interface_altsetting() to select the
 |  alternate setting (if there is more than one) of the interface used,
 |  and call the write() and read() method to send and receive data.
 |  When working in a new hardware, one first try would be like this:
 """
#dev = usb.core.find(idVendor=myVendorId, idProduct=myProductId)
#dev.set_configuration()
#dev.write(1, 'test')



