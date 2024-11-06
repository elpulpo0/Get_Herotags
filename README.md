### GET_Herotags

A simple API that allow you to get your needed herotags in one call.

```
http://127.0.0.1:5000/get_herotags?addresses=erdaddress111111,erdaddress222222,erdaddress333333
```

Response will look like

```json
[
  {
    "address": "erdaddress111111",
    "herotag": "address1"
  },
  {
    "address": "erdaddress222222",
    "herotag": "address2"
  },
  {
    "address": "erdaddress333333",
    "herotag": "address3",
  }
]
