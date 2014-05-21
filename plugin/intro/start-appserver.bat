@echo off

echo "---"
echo "Starting app server '${container.name}'..."
ping 127.0.0.1 -n 4 > nul
echo "Done."
