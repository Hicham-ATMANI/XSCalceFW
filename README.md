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

- Propagation of uncertainties and evaluate the correlation between bins using toys:

<img width="724" alt="Screenshot 2020-08-25 at 12 13 22" src="https://user-images.githubusercontent.com/53044514/91162462-6460be00-e6cc-11ea-9433-0e741c8f64da.png">

- Calculate the differential cross sections using the unfolded distributions: <br />


          <a href="https://www.codecogs.com/eqnedit.php?latex=\frac{d&space;\sigma_{i}}{d&space;x^{i}}=\frac{N_{Unf}^{i}}{\Delta&space;x^{i}&space;\mathcal{L}}&space;\cdot&space;=\frac{1}{A_{c}}&space;\frac{1}{\Delta&space;x^{i}&space;\mathcal{L}&space;}&space;\cdot&space;\Sigma_{j}&space;{M_{i&space;j}^{-1}&space;}&space;(N_{\mathrm{reco}}^{j}-N_{\mathrm{reco},&space;\mathrm{bkg}}^{j})" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\frac{d&space;\sigma_{i}}{d&space;x^{i}}=\frac{N_{Unf}^{i}}{\Delta&space;x^{i}&space;\mathcal{L}}&space;\cdot&space;=\frac{1}{A_{c}}&space;\frac{1}{\Delta&space;x^{i}&space;\mathcal{L}&space;}&space;\cdot&space;\Sigma_{j}&space;{M_{i&space;j}^{-1}&space;}&space;(N_{\mathrm{reco}}^{j}-N_{\mathrm{reco},&space;\mathrm{bkg}}^{j})" title="\frac{d \sigma_{i}}{d x^{i}}=\frac{N_{Unf}^{i}}{\Delta x^{i} \mathcal{L}} \cdot =\frac{1}{A_{c}} \frac{1}{\Delta x^{i} \mathcal{L} } \cdot \Sigma_{j} {M_{i j}^{-1} } (N_{\mathrm{reco}}^{j}-N_{\mathrm{reco}, \mathrm{bkg}}^{j})" /></a>

<img width="724" alt="Screenshot 2020-08-25 at 12 20 47" src="https://user-images.githubusercontent.com/53044514/91163163-7000b480-e6cd-11ea-9cd6-30e9bcd52402.png">


