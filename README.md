```
How to run:
```

make (to build the RooUnfold shared library)

python run/Unfolding.py

```
What it does:
```

This framework is used for the measurement of the differential cross sections for W-boson:

- Make control plots comparing data and simulation:

<img width="703" alt="Screenshot 2020-08-25 at 11 54 59" src="https://user-images.githubusercontent.com/53044514/91160658-f915ec80-e6c9-11ea-8af1-cefb7bd24ff9.png">

- Unfoled data distributions using the RooUnfold library:

<img width="724" alt="Screenshot 2020-08-25 at 12 00 52" src="https://user-images.githubusercontent.com/53044514/91161149-a7ba2d00-e6ca-11ea-9eb7-7db196983a8c.png">

- Calculate the <a href="https://www.codecogs.com/eqnedit.php?latex=\chi^{2}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\chi^{2}" title="\chi^{2}" /></a> value between data and simulation (templates), without correlation, defined as: <br />
