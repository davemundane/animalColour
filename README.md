# animalColour
slack app for creating project names

New projects were given code names containing a colour and an animal, discussions always resulted in disagreements. 

This app is designed to overcome that, by creating randomised names on request. 

To use, run it on a server that can reach the slack API: 

Either run the app directly
```
python animalColour.python
```

Or build a docker image
```
docker build -t slackapp . 
docker run --detach slackapp
```