# Assemble

| No. | Max | Min | Unit | Description |
| --- | --- | --- | --- | --- |
| O56 | 4095 | 0 | - | The maximum pedal input when position 2, value > O57 |
| O57 | 4095 | 0 | - | The pedal input of border between position 2 and position 1, O56 < O58 |
| O58 | 4095 | 0 | - | The pedal input of border between position 1 and position 0, O57 < O59 |
| O59 | 4095 | 0 | - | The pedal input of border between position 0 and position -1, O58 < O60 |
| O60 | 4095 | 0 | - | The pedal input of border between position -2 and position -1, O59 < O61 |
| O61 | 4095 | 0 | - | The minimum pedal input when position -2, O61 < O60 |
| O63 | 5 | 0 | - | The relation of pedal input and speed:<br> 0 = Linear;<br> 1 = 2 lines;<br> 2 = Curve(start slowly, end fast);<br/> 3 = Curve(start fast, end slowly);<br/> 4 = S curve(start slowly, middle fast, end slowly);<br/> 5 = S curve(start fast, middle slowly, end fast) |
| O08 | 1 | 0 | - | Type of the pedal:<br>0 = SilverStar's analog pedal;<br>1 = Standing operation pedla |
| O80 | 3 | 1 | - | Type of the keypad:<br>1 = Six keys;<br>2 = Seven keys;<br>3 = Twelve keys |
