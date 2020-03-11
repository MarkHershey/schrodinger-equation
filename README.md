# Schrodinger Equation

## Dependencies

```
python3 -V

>>> 3.5.0 and above
```

```
pip3 install numpy
pip3 install scipy
pip3 install mayavi
pip3 install PyQt5
```

## Visualisation

| n | l | m | 3D View | Section |
| :---: | :---: | :---: | :---: | :---: |
| 1 | 0 | 0 | <img src="figs/3dView/3d_0.png" height=auto width=auto> | <img src="figs/SectionView/Sec_0.png" height=auto width=auto> |
| 2 | 0 | 0 | <img src="figs/3dView/3d_1.png" height=auto width=auto> | <img src="figs/SectionView/Sec_1.png" height=auto width=auto> |
| 2 | 1 | 1 | <img src="figs/3dView/3d_2.png" height=auto width=auto> | <img src="figs/SectionView/Sec_2.png" height=auto width=auto> |
| 2 | 1 | 0 | <img src="figs/3dView/3d_3.png" height=auto width=auto> | <img src="figs/SectionView/Sec_3.png" height=auto width=auto> |
| 2 | 1 | -1 | <img src="figs/3dView/3d_4.png" height=auto width=auto> | <img src="figs/SectionView/Sec_4.png" height=auto width=auto> |
| 3 | 0 | 0 | <img src="figs/3dView/3d_5.png" height=auto width=auto> | <img src="figs/SectionView/Sec_5.png" height=auto width=auto> |
| 3 | 1 | 1 | <img src="figs/3dView/3d_6.png" height=auto width=auto> | <img src="figs/SectionView/Sec_6.png" height=auto width=auto> |
| 3 | 1 | 0 | <img src="figs/3dView/3d_7.png" height=auto width=auto> | <img src="figs/SectionView/Sec_7.png" height=auto width=auto> |
| 3 | 1 | -1 | <img src="figs/3dView/3d_8.png" height=auto width=auto> | <img src="figs/SectionView/Sec_8.png" height=auto width=auto> |
| 3 | 2 | 2 | <img src="figs/3dView/3d_9.png" height=auto width=auto> | <img src="figs/SectionView/Sec_9.png" height=auto width=auto> |
| 3 | 2 | 1 | <img src="figs/3dView/3d_10.png" height=auto width=auto> | <img src="figs/SectionView/Sec_10.png" height=auto width=auto> |
| 3 | 2 | 0 | <img src="figs/3dView/3d_11.png" height=auto width=auto> | <img src="figs/SectionView/Sec_11.png" height=auto width=auto> |
| 3 | 2 | -1 | <img src="figs/3dView/3d_12.png" height=auto width=auto> | <img src="figs/SectionView/Sec_12.png" height=auto width=auto> |
| 3 | 2 | -2 | <img src="figs/3dView/3d_13.png" height=auto width=auto> | <img src="figs/SectionView/Sec_13.png" height=auto width=auto> |
| 4 | 0 | 0 | <img src="figs/3dView/3d_14.png" height=auto width=auto> | <img src="figs/SectionView/Sec_14.png" height=auto width=auto> |
| 4 | 1 | 1 | <img src="figs/3dView/3d_15.png" height=auto width=auto> | <img src="figs/SectionView/Sec_15.png" height=auto width=auto> |
| 4 | 1 | 0 | <img src="figs/3dView/3d_16.png" height=auto width=auto> | <img src="figs/SectionView/Sec_16.png" height=auto width=auto> |
| 4 | 1 | -1 | <img src="figs/3dView/3d_17.png" height=auto width=auto> | <img src="figs/SectionView/Sec_17.png" height=auto width=auto> |
| 4 | 2 | 2 | <img src="figs/3dView/3d_18.png" height=auto width=auto> | <img src="figs/SectionView/Sec_18.png" height=auto width=auto> |
| 4 | 2 | 1 | <img src="figs/3dView/3d_19.png" height=auto width=auto> | <img src="figs/SectionView/Sec_19.png" height=auto width=auto> |
| 4 | 2 | 0 | <img src="figs/3dView/3d_20.png" height=auto width=auto> | <img src="figs/SectionView/Sec_20.png" height=auto width=auto> |
| 4 | 2 | -1 | <img src="figs/3dView/3d_21.png" height=auto width=auto> | <img src="figs/SectionView/Sec_21.png" height=auto width=auto> |
| 4 | 2 | -2 | <img src="figs/3dView/3d_22.png" height=auto width=auto> | <img src="figs/SectionView/Sec_22.png" height=auto width=auto> |
| 4 | 3 | 3 | <img src="figs/3dView/3d_23.png" height=auto width=auto> | <img src="figs/SectionView/Sec_23.png" height=auto width=auto> |
| 4 | 3 | 2 | <img src="figs/3dView/3d_24.png" height=auto width=auto> | <img src="figs/SectionView/Sec_24.png" height=auto width=auto> |
| 4 | 3 | 1 | <img src="figs/3dView/3d_25.png" height=auto width=auto> | <img src="figs/SectionView/Sec_25.png" height=auto width=auto> |
| 4 | 3 | 0 | <img src="figs/3dView/3d_26.png" height=auto width=auto> | <img src="figs/SectionView/Sec_26.png" height=auto width=auto> |
| 4 | 3 | -1 | <img src="figs/3dView/3d_27.png" height=auto width=auto> | <img src="figs/SectionView/Sec_27.png" height=auto width=auto> |
| 4 | 3 | -2 | <img src="figs/3dView/3d_28.png" height=auto width=auto> | <img src="figs/SectionView/Sec_28.png" height=auto width=auto> |
| 4 | 3 | -3 | <img src="figs/3dView/3d_29.png" height=auto width=auto> | <img src="figs/SectionView/Sec_29.png" height=auto width=auto> |
