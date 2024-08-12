# Project-Training-bot

## How does the Algorithm work

### Research

First of all we have to outline basic terminology used for our training algorithm.

#### Zones

What is a zone? A zone is a target range of effort. Usually we will use power to measure this however heart rate can also be used. Power zones we will use are as followed using the Dr Andrew Coggan's Zones as outlined on [Trainingpeaks](https://www.trainingpeaks.com/blog/power-training-levels/), one of the largest coach to athlete training platforms used by most professionals. Each of the following is expressed as a % of the riders FTP (Functional Threshold Power) more on that later.

```
       Z1 < 55%
56%  < Z2 < 75%
76%  < Z3 < 90%
91%  < Z4 < 105%
106% < Z5 < 120%
121% < Z6
       Z7   Max
```

In general though to quantify Z7 we will take Z6 < 200% and Z7 to be anything above that.

```
       Z1 < 55%
56%  < Z2 < 75%
76%  < Z3 < 90%
91%  < Z4 < 105%
106% < Z5 < 120%
121% < Z6 < 200%
201% < Z7   
```

Realistically speaking most efforts that are Z6/Z7 can be quantified as a joint zone.

#### FTP

What is FTP? Well it is the metric of how much power can be sustained for 1 hr. However due to max 1 hr efforts being difficult to conduct (take out to much energy out of the rider with comparitively little additional training benefit), we will focus on eFTP or estimate functional threshold power. We will use the power curver calculator provided by [FastFitness.Tips](https://www.cyclingapps.net/calculators/curve/), to measure our current eFTP to see how to improve performance, however we will add regular testing (Once every 2-3 months or so to provide more accurate estimates).

#### MAP

MAP is maximum aerobic power, the most amount of power we can produce while using oxygen to produce energy. However more generally for an easier calculation it is the most amount of power we can sustain for 5 minutes.

#### AC

Anaerobic capacity, is made up of 2 parts, anaerobic power which is the maximum amount of power able to produce anaerboically (generally speaking for efforts longer than 10 seconds) and anaerboic stamina how long can you sustain an effort for anaerboically ([Read more detail at High North](https://www.highnorth.co.uk/articles/anaerobic-training-cycling/)). If we represent these two metric on a graph we will gain a curve of which is visual representation of the anaerboic capacity. This curve forms part of a larger curve known as critical power curve. (More on that later).

#### NM

NM or Neuromusular Power is basically the maximum power your body can produce.

#### CP

Critical power is the point on a critical power graph where your body should theoretically hold this power indefinately. Unfortunately, in practice it is around the point for which your body can sustain the effort for 30 minutes. Ultimately, critical power can be described as being made up of two things (W' and CP itself). W' is the amount of work or energy that can be done above your critical power and we already know what CP is. This gives us a much better all round metric for one person rather than just the metrics above. However, we can also use the metrics above along with critical power to see if there are any weaknesses in the rider.

#### TSS

Training stress score is a number assigned to each ride created by trainingpeaks based upon how hard the ride was using power and your ftp as the 2 metrics.

##### CTL

Chronic Training Load is the measure of your general fitness also created by [Trainingpeaks](https://www.trainingpeaks.com/coach-blog/a-coachs-guide-to-atl-ctl-tsb/). It is the 42 day average of all your daily TSS.

##### ATL

Acute Training Load is the measure of your fatigue also created by [Trainingpeaks](https://www.trainingpeaks.com/coach-blog/a-coachs-guide-to-atl-ctl-tsb/). It is the 7 day average of all your daily TSS.

##### TSB

Training Stress Balance is your form metric also created by [Trainingpeaks](https://www.trainingpeaks.com/coach-blog/a-coachs-guide-to-atl-ctl-tsb/). And is your CTL - ATL. If your TSB is between around +15 and +25 you are in peak form, and ideally for a training block you want to sit between -10 and -30 depending on your fitness. But generally speaking you do not want to drop below -30 as you are at serve risk of illness.

#### Power to Weight

It is as simple as it sounds it is the ratio of power to the weight measured in W/kg. Generally speaking this is the most important metric for climbing rather than raw power.

These are more generally the basic metrics and terms being used for our training. We will now introduce some important conciderations for our alogrithm.

#### Fatigue

Firstly, how fatigued is a rider after a session and what is needed to recover. We will generally split this into 2 main categories intervals, and base. Interval sessions are one where structured efforts are done. Base is where the rider just rides steady usually in Zone 1/2.

##### Base

Base fatigue can be measure through those metrics by training peaks mainly (TSB). This will allow us to have a very easy understanding of the level of fatigue.

##### Intervals

Intervals is a bit more tricky to calculate. Scientist have found that at least one day is required between intervals, and two might be necessary for some people after some interval sessions. To figure out the number of rest days required we will measure the compliance with the workout (how close they were to the designated power numbers in the intervals) to decided if one or two days is needed. (95%+ 1, 80%+ 2, anything less will change the current week to a rest week.)

##### Block length planning

Generally, 3 hard weeks to 1 easy week block will be used (3:1 rule) as it allows time for the body to recover while training. As much as this isn't so important anymore, it allows for the rider to get good mental and physical rest.

#### What training to do?

We will decide what training to do based upon our fatigue for intervals and base. Using this and the persons schedule we will be able to have a good idea on whether the rider should be doing a base or intervals session. Additionally during the easy week we will do no interval sessions. We will also have 1 rest day a week for a similar reason to why we have a 3:1 rule.

#### What intervals to do?

We will use a base, polarized and potentially HIT way of scheduling our training. Base is where we spend all our time at Z1/Z2. It is ideal for beginners, what we are going to use it for. Polarized is where we spend 70% at Z1/2, 10% at Z3/4, 20% at Z5+. This is idedal for most people who already have fitness and want to work on becoming strong across all power ranges. As much as HIT (50% at Z1/2, 10% at Z3/4, 40% at Z5+) does have the potential to be more beneficial than Polarized the risk of burn out is too great for anyone to consistently train at it for a long time, however, it might be worth integrating just before a rest week, for someone on a lower time schedule or we can go inbetween a polarized and hiit. Since this is just the research and the algorithm isn't set in stone this might be updated later.

This works out at around 3/4 Rest, Recovery or Base days, 1 Threshold day, and 2 Vo2 Max or AC or NM days.

Since we have different types of riders, and we use different powers, as much as the ratios don't really change, the sessions in Z3/4 and Z5/6 change, for the following 5 main riders:

##### Climber - Anywhere from 1 minute -> Around An Hr

Z3/4 Efforts:

* Spend little time in Z3 maybe once a 4 week block tops.
* Spend most the time in Z4.

Z4/5 Efforts:

* Spend a lot of time in Z5 once or twice a week.
* Spend a bit of time in Z6, every other week, but co-ordinate it so there is 2 lots of Z6 in each block.
* No structured time in Z7, maybe add the odd sprint session for some sharpening up into a group ride but nothing set in stone.

##### TT Specialist - Anywhere from 10 minutes -> 2 Hrs

Z3/4 Efforts:

* Spend a bit of time in Z3 at least one session in a 4 week block.
* Spends most the time in Z4.

Z4/5 Efforts:

* Spend a lot of time in Z5 once or twice a week.
* Spend a little time in Z6, at most one session a block.
* No time in Z7.

##### All Rounder -> Everything a bit of sprinting, TTs, Long distance rides and Climbs.

Z3/4 Efforts:

* Spend half the time in Z3.
* Spend half the time in Z4.

Z4/5 Efforts:

* Spend half of the time in Z5, once a week.
* Spend alternating weeks in Z6, every other week. Aim for twice a block.
* Spend alternating weeks in Z7, every other week. Aim for once a block + the odd town sign sprint on group rides.

##### Sprinter - Aiming for efforts between 20 seconds -> 1 minute

Z3/4 Efforts:

* Spend half the time in Z3.
* Spend half the time in Z4.

Z4/5 Efforts:

* Spend alternating weeks in Z5, every other week. Aim for once a block.
* Spend alternating weeks in Z6, every other week. Aim for twice a block.
* Spend half the time in Z7, once a week.

##### Introduction - Long distance rides

This is the only one where we are going to reduce all efforts to just starting with base miles. This could also be useful for someone just wanting to ride their bike, but I wouldn't structure their training with this program.

#### Total Hours

Now for many people a big question would be well how many hours do I need to pack all this training in? For the average person 6-9hrs is plenty to see the benefit. With only really 10-12 hrs being needed by those racing. As well as this most people racing can get by on 6-9hrs of training with ramping the training up to 10-12hrs for a block just outside the race season. Only really pros need to and have the physical capability to train more than 12hr weeks consistently.[Trainright](https://https://trainright.com/how-many-hours-should-cyclists-ride-fitness-performance-training/)

#### Does this method carry across sports, i.e. does it carry across running and swimming especially for a triathlon.

Simple anwser is yes, it does.

Longer anwser is if you plan on just doing swimming or just doing running, this training method works perfectly, most likely you will have to pace it based on speed or hr, and change the overall volume but other than that it would be an identical training plan. However if you do plan on multiple discaplines for duathlon or triathlon there are some considerations. Interval workouts for different discaplines shouldn't be placed on a "base" day for another sport otherwise your cardiac system is still getting that same taxing. As much as most plans will do this I don't believe it is recommended. One hard day of your two weakest discaplines a week would be recommened and one of each would be ideal but might be a bit too taxing.

#### Periodisation

Now periodisation is where at the start of the year we plan out what "blocks" or "phases" we are going to go through in the year. Instead since we are using a 3:1 rule for hard to easy weeks, we are going to use an increase in amount of Z3/4 and Z5/6 efforts and a decrease in base slightly across the year to the point where the rider wants to peak, from a 80/5/15 -> 70/7.5/22.5. We feel that this might not be quite the perfect peak but would lead very very close to it. We can then ramp it down slowly until the end of the race season where we start the ramp up for next season again.

#### Race Warm Ups

As much as this isn't super relevant to training it is quite relevant for the events we are training for. A lot of people will think that you need to do a long hard warm up, but a short (10-15 mins) easy (at 60% of ftp) will be just as effective as a super long or hard or both warm up. But noteably that personal prefence can also play a role in the mental side of the warm up. [FastFitness.Tips](https://www.cyclingapps.net/blog/how-did-we-get-warm-ups-so-wrong/)

#### Nutrition

Disclamer *This comes from many experts I have talked to in the past. Unfortunately I do not remember the names of most of them and am unsure who said what. For the purpose of this I will try to find the appropriate research to back it up otherwise it is all of memory.*

Many programs will suggest eating around 120+gs of carbs an hr during something like an ironman. Unfortunately this is both really hard to do and in theory impossible. In general there is 2 types of carbs fructose and glucose. We can generally only digest 60gs of carbs an hr of each type, however this takes a lot of training to get there. More over for a normal person, a more realistic amount for an untrained stomach is around 30gs combined an hr. Now not only this the amount of carbs to be digested an hr is also ditacted from the intensity. At a lower intensity only really 30gs of combined carbs an hr is really needed. At medium intensity it will be around 60gs of carbs (I'll stop saying combined carbs but if I say carbs I mean both types.) an hr. And at high intensities it will be around 90gs + an hr. It is also dictated on the length of your session as well. But moreover we will use the following chart as a good guide.

![](https://cdn-images-1.medium.com/max/800/0*lhbjE5rn2kugVU7V.jpg)

https://www.precisionhydration.com/

All the nutrition research seems to line up from the guys at [FastFitness.Tips](https://www.cyclingapps.net/blog/8-worst-race-day-nutrition-errors/) They have got a lot of good information as it seems to line up with experts I have talked to on all kinds of training information and therefore been used for most of my extra research and is almost all backed by research papers.

#### Strength Training

Unfortunately, I do not have enough experience in this realm to provide such detailed information on it. However, from research it seems that strength training can improve performance by around 5% for cyclist, but you only really need to do around 60 minutes a week to achieve this, and anything above 140 minutes or just over 2 hrs seems to do more damage than it benefits the body. [FastFitness.Tips](https://www.cyclingapps.net/blog/dont-do-more-than-3hrs-per-week-in-the-gym/) Unfortunately this study was quite small with just under 100 cyclist involved.  But there is also other benefits to strength training than just raw performance. It also a well known fact that it can improve efficency on the bike and help riders hold a better aero position so it might be worth doing.

### How is all this research going to help us.

#### Cycle only

1. Start by establishing a goal race, if there isn't we will not use periodisation and just stick to the 70/10/20 ratio all year around. And we will ask what type of rider they want to be - Sprinter, Climber, TT Specialist, All-Rounder, or New. And how many hrs, 3-5, 6/7, 8/9, 10-12
2. We then store this and use it to calculate what week the upcoming week is.
3. We then calculate the ratios for sessions using the information above and assign each day for the upcoming week.
4. We then query each days focus and hours against our workout database and use that to pick our workouts.
5. We then add strength training on easy and or rest days.
6. Then repeat.

#### Run Only

Same as cycle only except hours are lower. And TT specialist become Long distance and the rest stay.

#### Swim Only

Coming soon

#### Duathlon

Since with duathlon there is only really one type of person we will add a beginner and an advanced plan. Advanced will follow a similar to climber training and new will follow a similar to new.

1. Find out hours to train, 3-5, etc. And find out if running is focus or cycling 1:2 effort ratio for priority to other.
2. Then basically the same as bike except half the days are run and half are bike and one day is a brick run, i.e. bike followed by a run.

#### Triathlon

Coming soon

#### Additional information:

* Make sure to keep fueled well through rides and to fuel properly before them.
* If you have a power meter, it will provide accurate calorie readings, if you would like to structure to lose weight, or gain weight depending on the type of rider.
* Weight tracking features may come later at some point. Along with adjustable schedule.
