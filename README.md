# Schrodinger Equation

## Dependencies

```
python3 --version

>>> 3.5.0 and above
```

```
pip3 install --upgrade numpy
pip3 install --upgrade scipy
pip3 install --upgrade mayavi
pip3 install --upgrade PyQt5
```

## Orbital Visualisation
> **n**: Principal Quantum Number
>
> **l**: Angular Momentum Quantum Number
>
> **m**: Magnetic Quantum Number

| n | l | m | Orbital | 3D View | Section View |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | 0 | 0 | 1s | <img src="figs/3dView/3d_0.png" height=auto width=auto> | <img src="figs/SectionView/Sec_0.png" height=auto width=auto> |
| 2 | 0 | 0 | 2s | <img src="figs/3dView/3d_1.png" height=auto width=auto> | <img src="figs/SectionView/Sec_1.png" height=auto width=auto> |
| 2 | 1 | 1 | 2p<sub>x</sub> | <img src="figs/3dView/3d_2.png" height=auto width=auto> | <img src="figs/SectionView/Sec_2.png" height=auto width=auto> |
| 2 | 1 | 0 | 2p<sub>z</sub> | <img src="figs/3dView/3d_3.png" height=auto width=auto> | <img src="figs/SectionView/Sec_3.png" height=auto width=auto> |
| 2 | 1 | -1 | 2p<sub>y</sub> | <img src="figs/3dView/3d_4.png" height=auto width=auto> | <img src="figs/SectionView/Sec_4.png" height=auto width=auto> |
| 3 | 0 | 0 | 3s | <img src="figs/3dView/3d_5.png" height=auto width=auto> | <img src="figs/SectionView/Sec_5.png" height=auto width=auto> |
| 3 | 1 | 1 | 3p<sub>x</sub> | <img src="figs/3dView/3d_6.png" height=auto width=auto> | <img src="figs/SectionView/Sec_6.png" height=auto width=auto> |
| 3 | 1 | 0 | 3p<sub>z</sub> | <img src="figs/3dView/3d_7.png" height=auto width=auto> | <img src="figs/SectionView/Sec_7.png" height=auto width=auto> |
| 3 | 1 | -1 | 3p<sub>y</sub> | <img src="figs/3dView/3d_8.png" height=auto width=auto> | <img src="figs/SectionView/Sec_8.png" height=auto width=auto> |
| 3 | 2 | 2 | 3d<sub>x<sup>2</sup>-y<sup>2</sup></sub> | <img src="figs/3dView/3d_9.png" height=auto width=auto> | <img src="figs/SectionView/Sec_9.png" height=auto width=auto> |
| 3 | 2 | 1 | 3d<sub>yz</sub> | <img src="figs/3dView/3d_10.png" height=auto width=auto> | <img src="figs/SectionView/Sec_10.png" height=auto width=auto> |
| 3 | 2 | 0 | 3d<sub>z<sup>2</sup></sub> | <img src="figs/3dView/3d_11.png" height=auto width=auto> | <img src="figs/SectionView/Sec_11.png" height=auto width=auto> |
| 3 | 2 | -1 | 3d<sub>xz</sub> | <img src="figs/3dView/3d_12.png" height=auto width=auto> | <img src="figs/SectionView/Sec_12.png" height=auto width=auto> |
| 3 | 2 | -2 | 3d<sub>xy</sub> | <img src="figs/3dView/3d_13.png" height=auto width=auto> | <img src="figs/SectionView/Sec_13.png" height=auto width=auto> |
| 4 | 0 | 0 | 4s | <img src="figs/3dView/3d_14.png" height=auto width=auto> | <img src="figs/SectionView/Sec_14.png" height=auto width=auto> |
| 4 | 1 | 1 | 4p<sub>x</sub> | <img src="figs/3dView/3d_15.png" height=auto width=auto> | <img src="figs/SectionView/Sec_15.png" height=auto width=auto> |
| 4 | 1 | 0 | 4p<sub>z</sub> | <img src="figs/3dView/3d_16.png" height=auto width=auto> | <img src="figs/SectionView/Sec_16.png" height=auto width=auto> |
| 4 | 1 | -1 | 4p<sub>y</sub> | <img src="figs/3dView/3d_17.png" height=auto width=auto> | <img src="figs/SectionView/Sec_17.png" height=auto width=auto> |
| 4 | 2 | 2 | 4d<sub>x<sup>2</sup>-y<sup>2</sup></sub> | <img src="figs/3dView/3d_18.png" height=auto width=auto> | <img src="figs/SectionView/Sec_18.png" height=auto width=auto> |
| 4 | 2 | 1 | 4d<sub>yz</sub> | <img src="figs/3dView/3d_19.png" height=auto width=auto> | <img src="figs/SectionView/Sec_19.png" height=auto width=auto> |
| 4 | 2 | 0 | 4d<sub>z<sup>2</sup></sub> | <img src="figs/3dView/3d_20.png" height=auto width=auto> | <img src="figs/SectionView/Sec_20.png" height=auto width=auto> |
| 4 | 2 | -1 | 4d<sub>xz</sub> | <img src="figs/3dView/3d_21.png" height=auto width=auto> | <img src="figs/SectionView/Sec_21.png" height=auto width=auto> |
| 4 | 2 | -2 | 4d<sub>xy</sub> | <img src="figs/3dView/3d_22.png" height=auto width=auto> | <img src="figs/SectionView/Sec_22.png" height=auto width=auto> |
| 4 | 3 | 3 | 4f<sub>y(3x<sup>2</sup>-y<sup>2</sup>)</sub> | <img src="figs/3dView/3d_23.png" height=auto width=auto> | <img src="figs/SectionView/Sec_23.png" height=auto width=auto> |
| 4 | 3 | 2 | 4f<sub>z(x<sup>2</sup>-y<sup>2</sup>)</sub> | <img src="figs/3dView/3d_24.png" height=auto width=auto> | <img src="figs/SectionView/Sec_24.png" height=auto width=auto> |
| 4 | 3 | 1 | 4f<sub>yz<sup>2</sup></sub> | <img src="figs/3dView/3d_25.png" height=auto width=auto> | <img src="figs/SectionView/Sec_25.png" height=auto width=auto> |
| 4 | 3 | 0 | 4f<sub>z<sup>3</sup></sub> | <img src="figs/3dView/3d_26.png" height=auto width=auto> | <img src="figs/SectionView/Sec_26.png" height=auto width=auto> |
| 4 | 3 | -1 | 4f<sub>xz<sup>2</sup></sub> | <img src="figs/3dView/3d_27.png" height=auto width=auto> | <img src="figs/SectionView/Sec_27.png" height=auto width=auto> |
| 4 | 3 | -2 | 4f<sub>xyz</sub> | <img src="figs/3dView/3d_28.png" height=auto width=auto> | <img src="figs/SectionView/Sec_28.png" height=auto width=auto> |
| 4 | 3 | -3 | 4f<sub>x(x<sup>2</sup>-3y<sup>2</sup>)</sub> | <img src="figs/3dView/3d_29.png" height=auto width=auto> | <img src="figs/SectionView/Sec_29.png" height=auto width=auto> |

`Created by Huang He (Mark) | 15 MAR 2020`
