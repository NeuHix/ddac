To crossmatch two catalogues we need to compare the angular distance between objects on the celestial sphere.
People loosely call this a **_"distance"_**, but technically it's an _Angular Distance_: the projected angle between objects as seen from Earth.

If we have an object on the celestial sphere with right ascension and declination $\left(\alpha_1, \delta_1\right)$ ,
then the angular distance to another object with coordinates $\left(\alpha_2, \delta_2\right)$ is:

$$
d=2 \arcsin \sqrt{\sin ^2 \frac{\left|\delta_1-\delta_2\right|}{2}+\cos \delta_1 \cos \delta_2 \sin ^2 \frac{\left|\alpha_1-\alpha_2\right|}{2}}
$$

Angular distances have the same units as angles (degrees). There are other equations for calculating
the angular distance but this one, called the haversine formula, is good at avoiding
floating point errors when the two points are close _together_.
