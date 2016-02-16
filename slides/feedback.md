## YANG Presentation 
- _DONE_ Repeated Eth0 (copy-n-paste error) in a few places I don’t think were intended
- Explain how servers advertise which features they support (OK – this was explained in the NETCONF tutorial later but perhaps forward reference/hint about it during YANG when explaining if-feature)
- Give guidance on the use/proliferation of if-features in IETF modules ?  The goal is to minimize them (not eliminate but use sparingly).   Or perhaps that is something for Andy’s guidelines doc ?
- It was mentioned that a “config false” list can exist without a key.  Perhaps explain a use case for that and give guidance on use of it in IETF modules ? Or again perhaps that is something for Andy’s guidelines doc ?
- Do you have the higher vs lower interface thing reversed ?  A vlan i/f would be on top of a physical interface  (so the lower level i/f for vlan0 is eth0).  Or maybe my understanding on this is wrong…
- You talked about ordering & leafrefs.  The referred-to object doesn’t have to exists *before* the referencing object.  Just not after (i.e. in a later edit-config).  They can both be in the same single edit-config (referred-to and referencing).
- I’m not sure that YANG allows a *combination* (tuple) of leafs to be unique.  Unique only applies to one leaf (at a time) right ?
 
## NETCONF Presentation
- Maybe more of a question about namespace.  In the example where we set the interface type the ‘type’ node is in the if namespace but the chosen value was from the if types namespace.
- There was a question about being able to <edit-config> interface * (wildcard) enabled = true.  It was said tht XPATH can do that but XPATH is a query (only used to retrieve) not for edit-config.  On a query, a wildcard exists by just using subtree filter without specifying a key value (just give the node name of the list itself).
- Aren’t there some known issues with granular locks ?  Not sure if we should advertise (verbally) that that capability exists ?
Granular locks are OK but the client does need to have some intelligence to use them.  If two clients C1 and C2 are both trying to lock branches A & B, and C1 gets a lock for A and C2 gets a lock for B, then they are both waiting to get the other lock they need.  The clients would need some sort of random backoff (where they release the locks if they can’t get them all and try again later).
 
