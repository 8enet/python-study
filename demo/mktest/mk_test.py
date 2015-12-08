import time


from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage 
device = MonkeyRunner.waitForConnection(100,'192.168.56.101:5555')

print(device.getSystemProperty('ro.build.description'))
time.sleep(10)
print('over')
# device.installPackage('/Users/zl/develop/project/MyApplication/test_package/build/outputs/apk/test_package-debug.apk')
# print 'install auccess !!'
# device.startActivity(component="com.example.testapp/com.example.testapp.MainActivity")
# # Takes a screenshot
# #result = device.takeSnapshot()
# # Writes the screenshot to a file
# #result.writeToFile('/Users/zl/develop/shotbegin.png','png')
# # Presses the Down button
# device.press('KEYCODE_DPAD_DOWN','DOWN_AND_UP')
# print 'KEYCODE_DPAD_DOWN'
# time.sleep(1)
#
# device.press('KEYCODE_DPAD_DOWN','DOWN_AND_UP')
# print 'KEYCODE_DPAD_DOWN'
# time.sleep(2)
# device.press('KEYCODE_DPAD_DOWN','DOWN_AND_UP')
# print 'KEYCODE_DPAD_DOWN'
# time.sleep(3)
# device.press('KEYCODE_DPAD_DOWN','DOWN_AND_UP')
# print 'KEYCODE_DPAD_DOWN'
# time.sleep(4)
# device.press('KEYCODE_DPAD_DOWN','DOWN_AND_UP')
# print 'KEYCODE_DPAD_DOWN'
# Takes a screenshot 
#result = device.takeSnapshot() 
# Writes the screenshot to a file 
#result.writeToFile('/Users/zl/develop/shotend.png','png')