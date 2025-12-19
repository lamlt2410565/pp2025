import subprocess

def run_command(cmd):
    if "|" in cmd:
        parts = [p.strip() for p in cmd.split("|")]
        p1 = subprocess.Popen(parts[0], shell=True, stdout=subprocess.PIPE)
        p2 = subprocess.Popen(parts[1], shell=True,
                              stdin=p1.stdout, stdout=subprocess.PIPE)
        output, _ = p2.communicate()
        print(output.decode(errors="ignore"))
        return
    
    stdin = None
    stdout = None

    if "<" in cmd:
        cmd, infile = cmd.split("<")
        stdin = open(infile.strip(), "r")

    if ">" in cmd:
        cmd, outfile = cmd.split(">")
        stdout = open(outfile.strip(), "w")

    subprocess.run(cmd.strip(), shell=True, stdin=stdin, stdout=stdout)

    if stdin:
        stdin.close()
    if stdout:
        stdout.close()


def main():
    while True:
        cmd = input("myshell> ").strip()
        if cmd == "exit":
            break
        if cmd:
            run_command(cmd)


if __name__ == "__main__":
    main()
