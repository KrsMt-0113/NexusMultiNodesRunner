import subprocess

CMD_TEMPLATE = "nexus-cli start --node-id {nodeid}"

with open("nodes.txt", "r", encoding="utf-8") as f:
    nodeids = [line.strip() for line in f if line.strip()]

session_name = "nodesession"

subprocess.run(["tmux", "new-session", "-d", "-s", session_name, CMD_TEMPLATE.format(nodeid=nodeids[0])])

for nodeid in nodeids[1:]:
    cmd = CMD_TEMPLATE.format(nodeid=nodeid)
    subprocess.run(["tmux", "new-window", "-t", session_name, cmd])

subprocess.run(["tmux", "attach-session", "-t", session_name])
