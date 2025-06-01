# Balloon Game


## Start the Server 

```bash
cd summit-25-fun-zone-artifacts/balloon-game/server
```

```bash
./balloon-popper server -k ./keys/jwt-private-key -p $(cat ./keys/.pass) -c ./config/users.json
```

Open the browser and navigate to <http://localhost:8080>  to access the web interface.

On a new terminal

### Start the Game

```bash
./start-game.sh
```

### Stop the Game

```bash
./stop-game.sh
```

## Dashboard

```bash
cd ~/balloon-popper-demo 
```

### Access Dashboard

```bash
task streamlit
```

Open the browser and navigate to <http://localhost:8501>  to access the dashboard.
