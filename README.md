# askbob-rasa
The Rasa server handling natural language queries for Ask Bob.

## Train

Train the model using the following command:

```bash
$ rasa train
```

## Run

First, run the actions server with the following command:

```bash
$ rasa run actions
```

Then, in another terminal, either run one of the following commands:

- To run on the command line to test things out,

```bash
$ rasa shell
```

- To run as a server to use with the Ask Bob voice client,

```bash
$ rasa run
```
