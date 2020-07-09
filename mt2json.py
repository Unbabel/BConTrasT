import sys
import json
import argparse
import os
from collections import defaultdict
import io
from itertools import cycle


def add_options(parser):
    group = parser.add_argument_group("Paths")
    group.add_argument("--agent-info", required=True, help="The path to the input file containing conversationID of the agent translations (should have the same number of lines as agent utterances provided in the agent-translations file).")
    group.add_argument("--agent-translations", required=True, help="The path to the input file containing agent translations (one utterance per line).")
    group.add_argument("--client-info", help="The path to the input file containing conversationID of the client translations (should have the same number of lines as client utterances provided in the client-translations file).")
    group.add_argument("--client-translations", help="The path to the input file containing client translations (one utterance per line).")
    group.add_argument("--json-input", required=True, help="The path to the original json file downloaded from the shared task webpage.")
    group.add_argument("--json-output", required=True, help="The path to the output json file containing the source sentences and translations.")
    group.add_argument("--with-client", dest="with_client", action="store_true", help="If you are submitting the translations of both the agenet and client.")


def load_files(info, translation):
    translations = defaultdict(list)
    with open(info, "r") as info_file, open(translation, "r") as trans_file:
        for cid, trans in zip(info_file, trans_file):
            translations[cid.strip()].append(trans.strip())
    return translations


def main():
    parser = argparse.ArgumentParser(description="MT2JSON")
    add_options(parser)

    args = parser.parse_args()
    with open(args.json_input, "r") as json_file:
        conversations = json.load(json_file)
    agent_translations = load_files(args.agent_info, args.agent_translations)
    if args.with_client:
        client_translations = load_files(args.client_info, args.client_translations)

    for cid in conversations:
        agent_iter = iter(agent_translations[cid])
        client_iter = iter(client_translations[cid]) if args.with_client else cycle([""])
        for uid, _ in enumerate(conversations[cid]):
            conversations[cid][uid]["target"] = next(agent_iter) if conversations[cid][uid]["speaker"] == "agent" else next(client_iter)
            
    with io.open(args.json_output, "w", encoding="utf-8") as out:
        json.dump(conversations, out, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    main()
