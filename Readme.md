# CURRENTLY UNDER DEVELOPMENT 

## Development tools installation
```bash
sudo python3 -m pip install pyqt5==5.14
sudo apt-get install pyqt5-dev-tools
sudo apt-get install qttools5-dev-tools
qtchooser -run-tool=designer -qt=5
```

## Execution
```bash
python3 src/sskmAnalyser.py
```

## Edit a *.ui file
```bash
designer -qt5 <path/to/ui/file>
```

## Generate code from ui file
```bash
pyuic5 <path/to/ui/file> > <path/to/py/file>
```