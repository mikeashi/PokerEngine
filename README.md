# PokerServer
Poker server with web GUI, where human and AI players can play poker holdem.

Poker Server is based on two projects:

- [PyPokerEngine](https://github.com/ishikota/PyPokerEngine).
- [PyPokerGUI](https://github.com/ishikota/PyPokerGUI).

Small changes have been made to the two projects, to make them compatible with [Pokershark](https://github.com/mikeashi/PokerShark).

# Configuration
The game configuration and bot players settings can be found under `Config`.


# None-Python AI Players

[Pokershark](https://github.com/mikeashi/PokerShark) is C# based, therefor we needed to develop an interface to communicat with the bot. The communication interface can be found under `Config\players\remote_player.py`, it uses RabbitMQ for RCP.

# Start server
This repository provides an easy to use docker image. To start container under windows you can use the provided "start.ps1" powershell script, to start under linux use the provided "start" bash script (SCRIPT NOT TESTED).

## web mode:

```
.\start.ps1 server
```

## cli mode:

```
.\start.ps1 cli
```
