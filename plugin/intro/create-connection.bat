@echo off

echo "---"
echo "Creating connection '${deployed.name}' on container '${deployed.container.name}'..."
ping 127.0.0.1 -n 4 > nul
echo "Done."
