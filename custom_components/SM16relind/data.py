FULL_NAME = "Sixteen RELAYS"
LINK = "https://sequentmicrosystems.com/products/sixteen-relays-8-layer-stackable-hat-for-raspberry-pi"

import SM16relind
API = SM16relind.SM16relind
DOMAIN = "SM16relind"
NAME_PREFIX = "sm16r"
SM_MAP = {
    "switch": {
        "relay": {
                "chan_no": 16,
                "com": {
                    "get": "get",
                    "set": "set"
                },
        }
    },
}
