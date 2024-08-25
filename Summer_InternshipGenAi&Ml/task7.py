from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

def set_volume(level):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    
    # Level should be between 0.0 and 1.0
    volume.SetMasterVolumeLevelScalar(level, None)
    print(f"Volume set to {level * 100}%")

# Example usage:
set_volume(0.5)  # Set volume to 50%
