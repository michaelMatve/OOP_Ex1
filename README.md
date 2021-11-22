# OOP_Ex1
## Assignment 1
### Literature

https://www.geeksforgeeks.org/smart-elevator-pro-geek-cup </br>
https://www.bjmc.lu.lv/fileadmin/user_upload/lu_portal/projekti/bjmc/Contents/8_4_12_Robal.pdf </br>
https://www.kone.co.il/he/Images/brochure-kone-destination_tcm203-18639.pdf </br>
https://www.cs.huji.ac.il/~ai/projects/2014/The_intelevator/files/report.pdf </br>

### Algorithm
First, we decided to create classes that will help us write the main algorithm, which will allocate an elevator to each call. </br>
the first class we chose to create is Elevator, that will represent a single elevator. the second class we created is CallForElev which represent a single call. the third class we created is AllCalls which holds a list of calls, and the number of calls. next, we created a Building class which represent a building.</br>
Then, we created an Algo class that gets file name of buildings, file name of calls, file name of the output. the class creates a building and a list of calls. we create a list of elevators, in addition we create 2 lists that will help us save information about every elevator. one of them will save the temporary start time, and the other will save the temporary calls the elevator is going to take. we also define a ratio that helps us decide the maximum number of calls we are going to add by running forward on the calls list. </br>
The main function in Algo class that will implement our algorithm and will allocate an elevator for each call and will create an output file is creatFile. we will allocate an elevator by running on every call every time we will allocate the elevator with the lowest finishing time to the call, and will run forward on the calls, and add calls with similar direction and source that is on the path. we will never add to many calls (more than the ratio we defined) because we want to create an equal balance. after that we will run all over again on the next call that wasn't allocated.  </br>
more detailed algorithm: </br>
1. first, we will run on all the calls from the first call </br>
2. for every call we will check if there was an elevator assigned to this call </br>
3. if it was assigned, we continue to the next call. if not, we will check the elevator with the lowest finishing time, and allocate this elevator to this call. </br>
4. now, we will run on all the other calls from this call. </br>
5. if it was assigned, we continue to the next call. if not, we will check if the call have the same direction as the current call, and if the call source is between the starting and ending floor in the temporary calls list. and if the call is up to the terms, we will check if the time we are passing by the call's source is bigger than the time the call was called. and if everything is true, we will add the call to the list of calls, and allocate the elevator to the call. </br>
6. the algorithm will stop running on the other calls when the algorithm will add more calls than the ratio, or when the algorithm is done running on all the calls.
7. then, the algorithm will check the next call, until it will get to the last one.

## UML

[https://github.com/michaelMatve/OOP_Ex1/blob/main/Uml.png?raw=true]