# hardware setup

## connections

power board j102 to microcontroller:

```
j102 pin 1 (ctrl_5v)    -> gpio 7 (digital out)
j102 pin 2 (ctrl_3v3)   -> gpio 8 (digital out)
j102 pin 3 (vsense_5v)  -> gpio 26 (adc in)
j102 pin 4 (vsense_3v3) -> gpio 27 (adc in)
j102 pin 5 (gnd)        -> gnd
j102 pin 6 (gnd)        -> gnd
```

## control signals

mosfets are active low:
- gpio low = rail on
- gpio high = rail off

## voltage sensing

voltage dividers (r101-r104):
- 5v rail reads as 2.5v
- 3.3v rail reads as 1.65v

adc range: 0-3.3v (16 bit)

## components

- u101: lm2596s-5 buck converter
- u102: ams1117-3.3 ldo
- q101, q102: p-channel mosfets
- r101-r104: 10k resistors
- c101-c104: capacitors

## power input

j101: 12v dc input
max current: 2a total

## supported boards

- raspberry pi pico
- raspberry pi pico w
- esp32
- esp32-s2/s3
- any micropython compatible board
