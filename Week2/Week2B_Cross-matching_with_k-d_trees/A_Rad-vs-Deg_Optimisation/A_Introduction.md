You may have noticed that crossmatching takes a long time, even with significantly cut down catalogues.

We've seen this before: **inefficient algorithms**.

The way we've implemented our crossmatcher means that for every object in BSS,  
we need to calculate distance to every object in SuperCOSMOS.  
Even our small crossmatching task requires 160 × 500 = 80,000 distance calculations.

With each distance calculation taking a few microseconds, it quickly adds up to seconds or minutes.  
Seconds may not seem like much but remember that the full SuperCOSMOS catalogue has 126 million objects,  
over 250,000 times larger than the truncated version we gave you to work with.

Then, imagine you were trying to crossmatch a catalogue other than AT20G BSS, with a size comparable to SuperCOSMOS.  
A crossmatching operation like that might take months or years.

We clearly need to be smarter about our choice of algorithm.

In this activity, we’ll look at modifying our previous crossmatcher to show you how easy it is to 
save computation time.