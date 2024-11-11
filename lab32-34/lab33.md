```dax
= if [Edad] >= 0 and [Edad] <= 18 then "0-18"
  else if [Edad] > 18 and [Edad] <= 35 then "19-35"
  else if [Edad] > 35 and [Edad] <= 60 then "36-60"
  else if [Edad] > 60 then "60+"
  else "Sin Especificar"
```
