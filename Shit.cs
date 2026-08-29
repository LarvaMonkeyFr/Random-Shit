using UnityEngine;

public class Shit : MonoBehaviour
{
    public bool DoShit = true;
    
    public void Start()
    {
        if (DoShit)
        {
          Debug.Log("Did Shit! :)");
        }
        else (!DoShit)
        {
          Debug.Log("Didn't do shit :(");
        }
    }
}

// Made by LarvaMonkey.
