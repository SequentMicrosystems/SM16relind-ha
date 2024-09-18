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
