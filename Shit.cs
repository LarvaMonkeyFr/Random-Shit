using UnityEngine;

public class Shit : MonoBehaviour
{
    public bool DoShit = true;

    // Changed this to Awake so it runs before other stuff.
    public void Awake()
    {
        if (DoShit)
        {
            DoingTheShit();
            Debug.Log("Did Shit! :)");
        }
        else
        {
            Debug.Log("Didn't do shit :(");
        }
    }

    public void DoingTheShit()
    {
    // CRASHHHHHHH
        while (DoShit)
        {
            Debug.Log("SHIT!");
        }
    }
}

// Made by LarvaMonkey.
