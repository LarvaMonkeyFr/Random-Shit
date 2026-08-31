using UnityEngine;

public class Shit : MonoBehaviour
{
    public bool DoShit = true;
    public bool DidShit = false;
    public int FinalNumber = 0;

    public void Awake()
    {
        if (DoShit)
        {
            DoingTheShit();
            Debug.Log("Doing the Shit...");
        }
        else
        {
            Debug.Log("Didn't do shit :(");
        }
    }

    public void DoingTheShit()
    {
        if (DoShit)
        {
            DoShit = false;
            DidShit = true;
            FinalNumber = FinalNumber + 1 * 5;
            Debug.Log("Did Shit! :)");
            Debug.Log("Btw, the answer is: " + FinalNumber);
        }
    }
}

// Made by LarvaMonkey.
