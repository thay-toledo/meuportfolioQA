import argparse

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--env", default="SuaTurma")

    args = parser.parse_args()

    return args

def get_environment():
    args = parse_arguments()
    print(f"Valor da variável env recebido: {args.env}\n===================================================")
    return args.env
