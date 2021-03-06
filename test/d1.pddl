(define (domain BLOCKS)
	(:requirements :strips :typing :negative-preconditions)

	(:types room ball gripper teste3 re t rm teste unused)

	(:constants left right - gripper)

	(:predicates
		(huahua - ball)
		(at ?b ?b2 - ball ?r ?r2 - room)
		(free ?g - gripper)

		(carry ?o - ball ?g - gripper ?t - teste)
					(at-robby1 ?from11 ?from113 - teste)
			(at-robby3 ?to4 - teste)
(at-robby4 ?to4 - teste)(at-robby5 ?to - teste)
(at-robby ?to4 - teste)
			(IRRA ?i ?i2 - teste)
(gripper ?gripper - gripper)
(ball ?obj - ball) (room ?room - room)
	)
  (:functions

     (road-length ?l1 ?l2 - location)
         (total-cost2)

     (total-cost ?ds - loc) - number3

  )
	(:action move
		:parameters  (?from1 ?from2 - t ?to22 - re ?t2 - teste3)
		:precondition 
		(and			(at-robby3 ?to4)

			(at-robby1 ?from131 ?from11)
			(not
			(at-robby3 ?to4)
			
			(at-robbyx4 ?from5 ?from6)
			)
		)
		:effect (and
(at-robby1 ?from11d ?from11)

(at-robby3 ?to3)(at-robby4 ?to4)(at-robby5 ?to)
			(at-robby3 ?to4)


			(not
			(at-robby3 ?to4)
			
			(at-robbyx4 ?from5 ?from6)
			)
		)
	)

	(:action pick
		:parameters (?roomAAA ?e3 - rm ?aaa - t)
		:precondition  (and 
			(at ?obj11 ?room11)
			(at-robby ?room)
			(free ?gripper)
		)
		:effect (and 
			(carry ?obj ?gripper)
			(IRRA ?i ?i2)






		)
	)

	(:action drop
		:parameters (?room ?room2 - room)
		:precondition (and (ball ?obj) (room ?room) (gripper ?gripper) (carry ?obj ?gripper) (at-robby ?room))
		:effect 
			(and 


				(at ?obj ?room) 
				

				(not (carry ?obj ?gripper)
					)
			)
	)
)




