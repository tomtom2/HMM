#include "somme_log.h"

double somme_log(double lp1, double lp2)
{
  double max;
  double min;
 
  if(lp1 > lp2)
    {
      max = lp1;
      min = lp2;
    }
  else
    {
      min = lp1;
      max = lp2;
    }
  if((max - min) < 50)
    return max + log(1 + exp(min - max));
 
  else
    return max;
}

double diff_log(double lp1, double lp2)
{

  if(lp1 > lp2){
    if((lp1 - lp2) < 50){
      return lp1 + log(1 - exp(lp2 - lp1));
    }
    else{
      return lp1;
    }

  }
  else{
    if((lp2 - lp1) < 50){
      return lp2 + log(exp(lp1 - lp2) - 1);
    }
    else{
      return -lp2;
    }
    
  }
}
