# power sequencer

python firmware for avionics power management board

## hardware

- raspberry pi pico or esp32
- custom power sequencer pcb
- 12v input, 5v + 3.3v outputs

## setup

1. flash micropython to your board
2. copy all .py files to board
3. connect hardware via 6-pin header

## pin connections

```
board pin -> power board j102
gpio 7    -> pin 1 (ctrl_5v)
gpio 8    -> pin 2 (ctrl_3v3)
gpio 26   -> pin 3 (vsense_5v)
gpio 27   -> pin 4 (vsense_3v3)
gnd       -> pin 5,6 (gnd)
```

## usage

### interactive mode
```python
import cli
cli.cli()
```

### programmatic
```python
import main

main.init()
main.power_on()
main.status()
main.power_off()
```

### monitoring
```python
import main

main.init()
main.power_on()
main.monitor_loop()  # runs forever
```

## commands

- `on` - turn on power rails
- `off` - turn off power rails
- `stat` - print voltage status
- `mon` - start monitoring mode
- `quit` - shutdown and exit

## testing

```python
import test
test.basic_test()
```

## safety features

- sequenced startup (5v first, then 3.3v)
- voltage monitoring every 500ms
- automatic shutdown on fault
- reverse order shutdown

## files

- `main.py` - core control logic
- `cli.py` - command line interface
- `test.py` - test suite
- `config.py` - hardware settings

## license

mit
