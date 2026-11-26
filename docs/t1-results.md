# T1 Goodsprings: proofs (T1.0)

Answers to the questions `docs/towns-design.md` sends to T1.0, with how each was found.

| Question | Answer | How |
| --- | --- | --- |
| Who reads `GoodspringsFaction` (00104C6E) in FalloutNV.esm? | Faction relations of GoodspringsAnimalFaction, GoodspringsFaction and GoodspringsRingoFaction; members DocMitchell, Chet, Easy Pete, Sunny, Trudy, the four GSSettler bases and VCG02GSSettler; one dialogue condition (INFO 0015E42A); scripts: VCG02 adds Ringo (INFO 00105D09); VMS16 `SetAlly GoodspringsFaction PlayerFaction` and `SetEnemy GoodspringsFaction PlayerFaction 1 1`; VMS16b (0015EC5B) removes Sunny, Trudy, Doc Mitchell and Easy Pete when the gangers win; 0010A214 `SetAlly GoodspringsFaction VVictorFaction` | a scan of every CTDA, SCRO, SNAM, XNAM, DATA subrecord and every script text for the FormID and the name |
| Is it safe for the mod's residents to join `GoodspringsFaction`? | Yes. Nothing counts the faction's members; the scripts only set its relation to the player and to Victor, which our residents should follow as the vanilla settlers do. When the gangers win, the one resident who stays (the gang-side hand) is removed from the faction by our town quest, as VMS16b does for the named NPCs | the list above |
| Are the Goodsprings homes' doors locked? | No. Both sides of every door of `GSHouseInterior01` to `04` have no lock data (XLOC absent) and no owner | the same scan, door references with XTEL into or out of the four homes |
| Does a persistent NPC follow its schedule while the player is away? | open: live test | |
| Does a text-only conversation package play? | open: live test | |
| Does the child race walk and sandbox? | open: live test | |
