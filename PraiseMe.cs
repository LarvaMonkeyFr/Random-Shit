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
        "Nya~ This game is soo good :3",
        "HMPH, stop thinking so bad about yourself. I belive in you :3"
    };

    public void Start()
    {
        if (praise)
        {
            int RandomMessage = Random.Range(0, PraiseMessages.Count);

            string RandomPraise = PraiseMessages[RandomMessage];

            Debug.Log(RandomPraise);
        }
        else
        {
            Debug.Error("ENABLE PRAISE RIGHT FUCKING NOW")
        }
    }
}
// Made by LarvaMonkey.
