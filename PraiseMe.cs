using UnityEngine;
using System.Collections.Generic;

public class PraiseMe : MonoBehaviour
{
    public bool praise = true;
    
    public List<string> PraiseMessages = new List<string>()
    {
        "You're such a good boy :3",
        "Oh my, keep coding for me :3",
        "Wow, I'm sooo proud of you :3"
    };

    public void Start()
    {
        if (praise)
        {
            int randomIndex = Random.Range(0, PraiseMessages.Count);

            string randomChoice = PraiseMessages[randomIndex];

            Debug.Log(randomChoice);
        }
        else
        {
            Debug.Log("ENABLE PRAISE RIGHT FUCKING NOW")
        }
    }
}
// Made by LarvaMonkey.
