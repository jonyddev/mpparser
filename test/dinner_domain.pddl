; This is a comment line
(define (domain dinner) ; There is no block comment like
  (:requirements :strips :negative-preconditions)
  (:predicates
    (clean)
    (dinner)
    (quiet)
    (present)
    (garbage)
    (unused)
  )
  (:action cook
    :parameters ()
    :precondition (and
      (clean)
    )
    :effect (and
      (dinner)
    )
  )
  (:action wrap
    :parameters ()
    :precondition (and
      (quiet)
    )
    :effect (and
      (present)
    )
  )
  (:action carry
    :parameters ()
    :precondition (and
      (garbage)
    )
    :effect (and
      (not (garbage)
      (clean)
      )
    )
  )
  (:action dolly
    :parameters ()
    :precondition (and
      (garbage)
    )
    :effect (and
      (not (garbage)
      (quiet))
    )
  )
  (:action dirty
    :parameters()
    :precondition
      (and
        (quiet)

      (not (garbage))
      )
    :effect
      (and
      (garbage)
      (not (quiet))
      )
  )
)