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

<img width="355" alt="Screenshot 2020-08-25 at 12 02 21" src="https://user-images.githubusercontent.com/53044514/91161287-dd5f1600-e6ca-11ea-8a8e-8fb64f9df1db.png"> <img width="350" alt="Screenshot 2020-08-25 at 12 05 22" src="https://user-images.githubusercontent.com/53044514/91161628-49417e80-e6cb-11ea-94b2-edb9d4476594.png">




- Unfoled data distributions using the RooUnfold library:

<img width="724" alt="Screenshot 2020-08-25 at 12 00 52" src="https://user-images.githubusercontent.com/53044514/91161149-a7ba2d00-e6ca-11ea-9eb7-7db196983a8c.png">

- Calculate the <a href="https://www.codecogs.com/eqnedit.php?latex=\chi^{2}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\chi^{2}" title="\chi^{2}" /></a> value between data and simulation (templates), without correlation, defined as: <br />
