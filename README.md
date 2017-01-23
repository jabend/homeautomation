# Home Automation files

These files are what I put together to support a very basic home automation projects.

The goal of the project was to integrate Amazon Alexa (echo) voice commands to control not-smart RF controlled outlets.

#Parts
* Westinghouse RF 3 Outlet Set (T28064 found @ Target for $1.99)
* Raspberry PI Zero
 * SD Card (2Gb with Raspian Jessie Lite) + Java
 * Network connection (USB WiFi or Ethernet will work)
* Amazon Echo (Only full size or Tap have "always listening" mic)
* GPIO Headers, Wire, Soldering Iron, Steady Hand, Patience. 

#Software
* HA Bridge (Emulates Philips Hue) installed on Pi https://github.com/bwssytems/ha-bridge
* Python script to trigger GPIO wired to Westinghouse RF Remote
