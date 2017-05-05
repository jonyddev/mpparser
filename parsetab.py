
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "DEFINE DOMAIN REQUIREMENTS TYPES CONSTANTS PREDICATES FUNCTIONS ACTION PARAMETERS PRECONDITION EFFECT FORALL EXISTS INCREASE DECREASE ASSIGN IMPLY PREFERENCE WHEN AGENT PROBLEM OBJECTS INIT GOAL CONDITION INITIAL STATE ACTIONS PRECONDITIONS PRECOND INITS AND NOT ID TYPEID ICONST FCONST SCONST CCONST NUM PLUS MINUS TIMES DIVIDE MOD OR XOR LSHIFT RSHIFT LOR LAND LNOT LT LE GT GE EQ NE EQUALS TIMESEQUAL DIVEQUAL MODEQUAL PLUSEQUAL MINUSEQUAL LSHIFTEQUAL RSHIFTEQUAL ANDEQUAL XOREQUAL OREQUAL PLUSPLUS MINUSMINUS VAR LPAREN RPAREN LBRACKET RBRACKET LBRACE RBRACE COMMA PERIOD SEMI COLON ELLIPSIS COMP ARROWprograma : LPAREN DEFINE domain_formalization RPAREN\n    programa : LPAREN DEFINE problem_formalization RPARENprograma : strips_formalizationprograma : adl_formalizationprograma : LPAREN DOMAIN RPARENadl_formalization : adl_initial_state adl_goal_state adl_actions_defadl_initial_state : error adl_goal_state adl_actions_defadl_initial_state : INIT LPAREN adl_lista_predicados RPARENadl_initial_state : INIT error adl_lista_predicados RPARENadl_lista_predicados : adl_strips_predicadoadl_lista_predicados : adl_strips_predicado AND adl_lista_predicadosadl_goal_state : GOAL LPAREN adl_lista_predicados RPARENadl_actions_def : adl_actionadl_actions_def : adl_action adl_actions_defadl_action : ACTION LPAREN ID LPAREN adl_lista_parametros RPAREN COMMA adl_precond adl_effect RPARENadl_lista_parametros : adl_parametroadl_lista_parametros : adl_parametro COMMA adl_lista_parametrosadl_parametro : ID COLON lista_idsadl_precond : PRECOND COLON adl_lista_predicadosadl_effect : EFFECT COLON adl_lista_predicadosstrips_formalization : strips_initial_state strips_goal_state strips_actions_defstrips_initial_state : INITS STATE COLON strips_lista_predicadosstrips_lista_predicados : adl_strips_predicadostrips_lista_predicados : adl_strips_predicado COMMA strips_lista_predicadosadl_strips_predicado : ID LPAREN adl_strips_lista_ids RPARENadl_strips_predicado : AND ID LPAREN adl_strips_lista_ids RPARENadl_strips_lista_ids : IDadl_strips_lista_ids : ID COMMA adl_strips_lista_idsstrips_goal_state : GOAL STATE COLON strips_lista_predicadosstrips_actions_def : strips_actions_def : ACTIONS COLON strips_lista_actionsstrips_lista_actions : strips_actionstrips_lista_actions : strips_action strips_lista_actionsstrips_action : adl_strips_predicado PRECONDITIONS COLON strips_lista_predicados EFFECT COLON strips_lista_predicadosproblem_formalization : def_problem def_domain_p def_objects def_init def_goaldef_problem : LPAREN PROBLEM ID RPARENdef_domain_p : LPAREN COLON DOMAIN ID RPARENdef_objects : LPAREN COLON OBJECTS lista_objects RPARENlista_objects : lista_objects : lista_ids MINUS ID lista_objectslista_objects : lista_idsdef_init : LPAREN COLON INIT lista_predicados_p RPARENdef_goal : def_goal : LPAREN COLON GOAL LPAREN AND lista_predicados_p RPAREN RPAREN\n                  def_goal : LPAREN COLON GOAL LPAREN NOT lista_predicados_p RPAREN RPARENdef_goal : LPAREN COLON GOAL COLON AGENT agent_def COLON CONDITION lista_predicados_p RPARENdef_goal : LPAREN COLON GOAL RPARENlista_predicados_p : lista_predicados_p : LPAREN lista_ids RPAREN lista_predicados_plista_predicados_p : LPAREN AND lista_predicados_p RPAREN lista_predicados_plista_predicados_p : LPAREN NOT lista_predicados_p RPAREN lista_predicados_plista_predicados_p : LPAREN COMP LPAREN lista_ids RPAREN NUM RPAREN lista_predicados_plista_predicados_p : LPAREN COMP LPAREN lista_ids RPAREN ID RPAREN lista_predicados_pdomain_formalization : def_domain def_requirements def_types def_constants def_predicates def_functions def_actionsdomain_formalization : def_domain def_requirements def_types def_predicates def_actionsdomain_formalization : def_domain def_requirements def_types def_predicates def_functions def_actionsdomain_formalization : def_domain def_requirements def_types def_constants def_predicates def_actionsdomain_formalization : def_domain def_requirements def_predicates def_actionsdef_domain : LPAREN DOMAIN ID RPARENdef_requirements : def_requirements : LPAREN COLON REQUIREMENTS lista_requirements RPARENlista_requirements : lista_requirements : COLON ID lista_requirementsdef_types : def_types : LPAREN COLON TYPES lista_types RPARENdef_types : LPAREN COLON TYPES lista_types MINUS ID RPARENlista_types : lista_types : ID lista_typesdef_constants : def_constants : LPAREN COLON CONSTANTS lista_constants RPARENlista_constants : lista_constants : lista_ids MINUS ID lista_constantsdef_predicates : def_predicates : LPAREN COLON PREDICATES lista_predicates RPARENlista_predicates : lista_predicates : LPAREN ID p_def RPAREN lista_predicatesp_def : lista_var MINUS ID p_defp_def : lista_vardef_functions : def_functions : LPAREN COLON FUNCTIONS lista_functions RPARENlista_functions : lista_functions : function lista_functionsfunction : LPAREN ID VAR ID MINUS ID RPARENfunction : LPAREN ID RPARENdef_actions : def_actions : LPAREN COLON ACTION ID a_def RPAREN def_actionsdef_actions : LPAREN COLON ACTION ID COLON AGENT agent_def a_def RPAREN def_actionsagent_def : IDagent_def : VAR IDagent_def : VAR ID MINUS IDa_def : a_def : COLON PARAMETERS LPAREN lista_parameters RPAREN COLON PRECONDITION pddl_preconditions COLON EFFECT pddl_effectspddl_preconditions : lista_preds_oppddl_effects : lista_preds_op lista_parameters : lista_parameters : VAR ID MINUS ID lista_parameterslista_parameters : lista_var MINUS ID lista_parameterslista_parameters : lista_var lista_preds_op : lista_preds_op : lista_predicadoslista_preds_op : LPAREN AND lista_preds_op RPAREN lista_preds_oplista_preds_op : LPAREN NOT lista_predicados RPAREN lista_preds_op : LPAREN FORALL lista_preds_op RPAREN lista_preds_op : LPAREN EXISTS lista_preds_op RPAREN lista_preds_op : LPAREN IMPLY lista_preds_op RPAREN lista_preds_op : LPAREN PREFERENCE '[' ID ']' RPAREN lista_preds_op : LPAREN WHEN lista_preds_op RPARENlista_predicados : LPAREN ID lista_var RPAREN lista_preds_oplista_predicados : LPAREN lista_var MINUS ID RPAREN lista_preds_oplista_predicados : LPAREN COMP lista_var RPAREN lista_preds_oplista_predicados : LPAREN VAR ID COMP ID RPAREN lista_preds_oplista_predicados : LPAREN DECREASE LPAREN ID RPAREN NUM RPARENlista_var : lista_var : VAR ID lista_varlista_var : ID lista_varlista_ids : lista_ids : ID lista_ids"
    
_lr_action_items = {'LPAREN':([0,9,10,15,23,24,31,38,44,46,57,62,63,66,73,80,81,82,83,89,100,103,108,122,135,137,141,148,152,156,158,161,170,171,184,185,186,187,193,197,198,199,201,204,205,207,217,231,232,253,260,270,271,272,273,284,285,286,287,288,291,295,310,311,317,320,328,334,],[2,18,20,32,45,47,51,58,64,67,77,84,86,90,95,-59,-36,101,104,112,124,86,132,86,-61,159,-37,168,-65,-74,180,-38,168,-70,159,159,210,-42,-80,222,86,-66,132,159,159,159,-84,159,159,86,159,159,159,-83,279,279,298,279,279,279,279,309,279,279,279,279,279,279,]),'INITS':([0,],[7,]),'error':([0,9,],[8,19,]),'INIT':([0,113,],[9,137,]),'$end':([1,3,4,12,25,26,29,30,42,43,50,54,69,70,72,93,96,99,120,212,234,],[0,-3,-4,-30,-5,-21,-6,-13,-1,-2,-14,-23,-31,-32,-29,-33,-24,-25,-26,-34,-15,]),'DEFINE':([2,],[10,]),'DOMAIN':([2,20,68,],[11,40,92,]),'GOAL':([5,6,8,30,34,50,53,54,55,59,96,99,120,136,234,],[13,15,15,-13,-7,-14,-22,-23,-8,-9,-24,-25,-26,158,-15,]),'STATE':([7,13,],[16,28,]),'RPAREN':([11,21,22,23,35,36,39,44,52,60,61,62,63,76,78,79,80,82,83,85,88,89,97,99,100,102,103,107,108,110,111,114,115,118,119,120,121,122,123,126,128,130,131,133,134,135,137,138,139,140,143,146,148,149,151,152,154,155,156,157,158,159,160,163,165,167,169,170,171,174,175,176,177,178,182,183,184,185,187,188,192,193,194,195,198,199,200,201,203,204,205,207,208,209,210,211,213,217,218,219,220,222,223,224,225,226,227,228,230,231,232,233,239,240,241,243,244,245,246,248,249,251,253,256,258,259,260,261,262,263,264,265,268,269,270,271,272,274,275,276,277,278,282,283,284,286,287,288,290,291,293,297,299,300,301,302,304,305,307,310,311,312,313,314,315,317,318,319,320,322,323,324,325,326,327,328,329,330,332,333,334,335,336,337,],[25,42,43,-60,55,-10,59,-64,74,80,81,-69,-85,-11,-27,99,-59,-73,-79,-58,-62,-43,120,-25,-79,-55,-85,-67,-75,135,-35,-39,141,144,-16,-26,-28,-85,-57,-56,-71,152,-67,156,-62,-61,-48,161,-41,-116,-116,-54,-81,171,-91,-65,-68,-113,-74,-63,182,-116,187,-117,-18,-17,193,-81,-70,198,199,-113,201,-78,-47,207,-48,-48,-42,-39,217,-80,-82,-71,-85,-66,-115,-75,-113,-48,-48,-48,231,232,-116,-40,234,-84,-72,-88,-91,-95,-86,-76,-113,-114,245,246,-49,-48,-48,250,253,-89,255,-98,-77,258,259,-50,-51,-20,-85,-113,-44,-45,-48,270,271,272,-87,-90,-95,276,-48,-48,-83,-95,-97,-46,-52,-53,-100,-96,-99,-99,-99,-99,-113,-99,-113,311,312,313,314,315,317,318,320,-99,-99,-102,-103,-104,-105,-99,-107,328,-99,331,-92,-94,-101,332,-108,-99,-110,334,-106,-109,-99,337,-111,-112,]),'ACTIONS':([12,54,72,96,99,120,],[27,-23,-29,-24,-25,-26,]),'ACTION':([14,17,30,74,106,127,147,234,],[31,31,31,-12,129,129,129,-15,]),'COLON':([16,27,28,45,47,64,67,84,86,88,90,94,101,104,112,117,124,134,151,158,164,191,214,219,220,229,240,255,265,273,280,281,282,311,312,313,314,315,317,318,320,325,327,328,329,332,333,334,336,337,],[33,48,49,65,68,87,91,105,106,109,113,116,125,127,136,143,147,109,173,181,189,215,235,-88,238,247,-89,266,-90,-99,296,-93,-100,-99,-102,-103,-104,-105,-99,-107,-99,-101,-108,-99,-110,-106,-109,-99,-111,-112,]),'ID':([18,19,32,33,37,40,41,48,49,51,54,56,58,70,75,77,92,95,96,98,99,107,109,114,116,120,128,129,131,132,140,143,145,153,155,159,162,168,172,176,179,188,189,195,196,202,203,206,210,212,215,216,221,222,225,235,242,250,252,254,256,257,267,268,274,279,290,293,294,298,303,306,308,309,321,],[38,38,38,38,57,60,61,38,38,73,-23,38,78,38,38,78,115,117,-24,78,-25,131,134,140,38,-26,140,151,131,155,140,140,117,175,176,140,188,192,195,176,203,140,38,140,219,225,176,219,140,-34,38,237,240,176,176,38,256,262,263,265,176,268,274,176,176,290,176,176,308,290,316,319,176,322,330,]),'AND':([18,19,32,33,36,48,49,54,56,70,75,96,99,116,120,159,180,189,212,215,235,279,],[37,37,37,37,56,37,37,-23,37,37,37,-24,-25,37,-26,184,204,37,-34,37,37,284,]),'PROBLEM':([20,],[41,]),'EFFECT':([36,54,76,96,99,120,142,190,236,296,],[-10,-23,-11,-24,-25,-26,164,214,-19,310,]),'COMMA':([54,78,99,119,120,140,143,144,163,165,],[75,98,-25,145,-26,-116,-116,166,-117,-18,]),'REQUIREMENTS':([65,],[88,]),'PRECONDITIONS':([71,99,120,],[94,-25,-26,]),'TYPES':([87,],[107,]),'PREDICATES':([87,105,125,],[108,108,108,]),'OBJECTS':([91,],[114,]),'CONSTANTS':([105,],[128,]),'MINUS':([107,114,128,130,131,139,140,150,154,155,163,176,178,188,195,200,203,222,225,226,237,240,243,256,268,274,279,290,292,298,304,308,],[-67,-116,-116,153,-67,162,-116,172,-68,-113,-117,-113,202,-116,-116,-115,-113,-113,-113,-114,252,254,257,267,-113,-113,-113,-113,306,-113,-115,-113,]),'FUNCTIONS':([127,147,],[148,148,]),'VAR':([155,176,192,196,203,206,222,225,256,268,274,279,290,293,298,308,],[179,179,216,221,179,221,242,179,179,242,242,294,179,179,294,179,]),'NOT':([159,180,279,],[185,205,285,]),'COMP':([159,279,298,308,],[186,293,293,321,]),'PRECOND':([166,],[191,]),'AGENT':([173,181,],[196,206,]),'PARAMETERS':([173,238,],[197,197,]),'CONDITION':([247,],[260,]),'NUM':([250,331,],[261,335,]),'PRECONDITION':([266,],[273,]),'FORALL':([279,],[286,]),'EXISTS':([279,],[287,]),'IMPLY':([279,],[288,]),'PREFERENCE':([279,],[289,]),'WHEN':([279,],[291,]),'DECREASE':([279,298,],[295,295,]),'[':([289,],[303,]),']':([316,],[326,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'strips_formalization':([0,],[3,]),'adl_formalization':([0,],[4,]),'strips_initial_state':([0,],[5,]),'adl_initial_state':([0,],[6,]),'strips_goal_state':([5,],[12,]),'adl_goal_state':([6,8,],[14,17,]),'domain_formalization':([10,],[21,]),'problem_formalization':([10,],[22,]),'def_domain':([10,],[23,]),'def_problem':([10,],[24,]),'strips_actions_def':([12,],[26,]),'adl_actions_def':([14,17,30,],[29,34,50,]),'adl_action':([14,17,30,],[30,30,30,]),'adl_lista_predicados':([18,19,32,56,215,235,],[35,39,52,76,236,251,]),'adl_strips_predicado':([18,19,32,33,48,49,56,70,75,116,189,215,235,],[36,36,36,54,71,54,36,71,54,54,54,36,36,]),'def_requirements':([23,],[44,]),'def_domain_p':([24,],[46,]),'strips_lista_predicados':([33,49,75,116,189,],[53,72,96,142,212,]),'def_types':([44,],[62,]),'def_predicates':([44,62,82,],[63,83,100,]),'def_objects':([46,],[66,]),'strips_lista_actions':([48,70,],[69,93,]),'strips_action':([48,70,],[70,70,]),'adl_strips_lista_ids':([58,77,98,],[79,97,121,]),'def_constants':([62,],[82,]),'def_actions':([63,83,100,103,122,198,253,],[85,102,123,126,146,223,264,]),'def_init':([66,],[89,]),'def_functions':([83,100,],[103,122,]),'lista_requirements':([88,134,],[110,157,]),'def_goal':([89,],[111,]),'adl_lista_parametros':([95,145,],[118,167,]),'adl_parametro':([95,145,],[119,119,]),'lista_types':([107,131,],[130,154,]),'lista_predicates':([108,201,],[133,224,]),'lista_objects':([114,188,],[138,211,]),'lista_ids':([114,128,140,143,159,188,195,210,],[139,150,163,165,183,139,150,233,]),'lista_constants':([128,195,],[149,218,]),'lista_predicados_p':([137,184,185,204,205,207,231,232,260,270,271,],[160,208,209,227,228,230,248,249,269,277,278,]),'lista_functions':([148,170,],[169,194,]),'function':([148,170,],[170,170,]),'a_def':([151,220,],[174,239,]),'p_def':([155,225,],[177,244,]),'lista_var':([155,176,203,222,225,256,268,274,279,290,293,298,308,],[178,200,226,243,178,226,243,243,292,304,307,292,226,]),'adl_precond':([166,],[190,]),'adl_effect':([190,],[213,]),'agent_def':([196,206,],[220,229,]),'lista_parameters':([222,268,274,],[241,275,283,]),'pddl_preconditions':([273,],[280,]),'lista_preds_op':([273,284,286,287,288,291,310,311,317,320,328,334,],[281,297,300,301,302,305,324,325,327,329,333,336,]),'lista_predicados':([273,284,285,286,287,288,291,310,311,317,320,328,334,],[282,282,299,282,282,282,282,282,282,282,282,282,282,]),'pddl_effects':([310,],[323,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> LPAREN DEFINE domain_formalization RPAREN','programa',4,'p_programa_1','multipparser.py',376),
  ('programa -> LPAREN DEFINE problem_formalization RPAREN','programa',4,'p_programa_2','multipparser.py',381),
  ('programa -> strips_formalization','programa',1,'p_programa_3','multipparser.py',385),
  ('programa -> adl_formalization','programa',1,'p_programa_4','multipparser.py',389),
  ('programa -> LPAREN DOMAIN RPAREN','programa',3,'p_programa_5','multipparser.py',393),
  ('adl_formalization -> adl_initial_state adl_goal_state adl_actions_def','adl_formalization',3,'p_adl_formalization_1','multipparser.py',403),
  ('adl_initial_state -> error adl_goal_state adl_actions_def','adl_initial_state',3,'p_adl_formalization_bad','multipparser.py',406),
  ('adl_initial_state -> INIT LPAREN adl_lista_predicados RPAREN','adl_initial_state',4,'p_adl_initial_state_1','multipparser.py',413),
  ('adl_initial_state -> INIT error adl_lista_predicados RPAREN','adl_initial_state',4,'p_initial_state_bad','multipparser.py',417),
  ('adl_lista_predicados -> adl_strips_predicado','adl_lista_predicados',1,'p_adl_lista_predicados_1','multipparser.py',423),
  ('adl_lista_predicados -> adl_strips_predicado AND adl_lista_predicados','adl_lista_predicados',3,'p_adl_lista_predicados_2','multipparser.py',427),
  ('adl_goal_state -> GOAL LPAREN adl_lista_predicados RPAREN','adl_goal_state',4,'p_adl_goal_state_1','multipparser.py',431),
  ('adl_actions_def -> adl_action','adl_actions_def',1,'p_adl_actions_def_1','multipparser.py',435),
  ('adl_actions_def -> adl_action adl_actions_def','adl_actions_def',2,'p_adl_actions_def_2','multipparser.py',439),
  ('adl_action -> ACTION LPAREN ID LPAREN adl_lista_parametros RPAREN COMMA adl_precond adl_effect RPAREN','adl_action',10,'p_adl_action_1','multipparser.py',443),
  ('adl_lista_parametros -> adl_parametro','adl_lista_parametros',1,'p_adl_lista_parametros_1','multipparser.py',447),
  ('adl_lista_parametros -> adl_parametro COMMA adl_lista_parametros','adl_lista_parametros',3,'p_adl_lista_parametros_2','multipparser.py',451),
  ('adl_parametro -> ID COLON lista_ids','adl_parametro',3,'p_adl_parametro_1','multipparser.py',455),
  ('adl_precond -> PRECOND COLON adl_lista_predicados','adl_precond',3,'p_adl_precond_1','multipparser.py',459),
  ('adl_effect -> EFFECT COLON adl_lista_predicados','adl_effect',3,'p_adl_effect_1','multipparser.py',462),
  ('strips_formalization -> strips_initial_state strips_goal_state strips_actions_def','strips_formalization',3,'p_strips_formalization_1','multipparser.py',465),
  ('strips_initial_state -> INITS STATE COLON strips_lista_predicados','strips_initial_state',4,'p_strips_initial_state_1','multipparser.py',469),
  ('strips_lista_predicados -> adl_strips_predicado','strips_lista_predicados',1,'p_strips_lista_predicados_1','multipparser.py',473),
  ('strips_lista_predicados -> adl_strips_predicado COMMA strips_lista_predicados','strips_lista_predicados',3,'p_strips_lista_predicados_2','multipparser.py',477),
  ('adl_strips_predicado -> ID LPAREN adl_strips_lista_ids RPAREN','adl_strips_predicado',4,'p_adl_strips_predicado_1','multipparser.py',481),
  ('adl_strips_predicado -> AND ID LPAREN adl_strips_lista_ids RPAREN','adl_strips_predicado',5,'p_adl_strips_predicado_2','multipparser.py',485),
  ('adl_strips_lista_ids -> ID','adl_strips_lista_ids',1,'p_adl_strips_lista_ids_1','multipparser.py',489),
  ('adl_strips_lista_ids -> ID COMMA adl_strips_lista_ids','adl_strips_lista_ids',3,'p_adl_strips_lista_ids_2','multipparser.py',493),
  ('strips_goal_state -> GOAL STATE COLON strips_lista_predicados','strips_goal_state',4,'p_strips_goal_state_1','multipparser.py',497),
  ('strips_actions_def -> <empty>','strips_actions_def',0,'p_strips_actions_def_1','multipparser.py',501),
  ('strips_actions_def -> ACTIONS COLON strips_lista_actions','strips_actions_def',3,'p_strips_actions_def_2','multipparser.py',504),
  ('strips_lista_actions -> strips_action','strips_lista_actions',1,'p_strips_lista_actions_1','multipparser.py',508),
  ('strips_lista_actions -> strips_action strips_lista_actions','strips_lista_actions',2,'p_strips_lista_actions_2','multipparser.py',512),
  ('strips_action -> adl_strips_predicado PRECONDITIONS COLON strips_lista_predicados EFFECT COLON strips_lista_predicados','strips_action',7,'p_strips_action_1','multipparser.py',516),
  ('problem_formalization -> def_problem def_domain_p def_objects def_init def_goal','problem_formalization',5,'p_problem_formalization_1','multipparser.py',520),
  ('def_problem -> LPAREN PROBLEM ID RPAREN','def_problem',4,'p_def_problem_1','multipparser.py',524),
  ('def_domain_p -> LPAREN COLON DOMAIN ID RPAREN','def_domain_p',5,'p_def_domain_p_1','multipparser.py',528),
  ('def_objects -> LPAREN COLON OBJECTS lista_objects RPAREN','def_objects',5,'p_def_objects_1','multipparser.py',532),
  ('lista_objects -> <empty>','lista_objects',0,'p_lista_objects_1','multipparser.py',536),
  ('lista_objects -> lista_ids MINUS ID lista_objects','lista_objects',4,'p_lista_objects_2','multipparser.py',539),
  ('lista_objects -> lista_ids','lista_objects',1,'p_lista_objects_3','multipparser.py',543),
  ('def_init -> LPAREN COLON INIT lista_predicados_p RPAREN','def_init',5,'p_def_init_1','multipparser.py',547),
  ('def_goal -> <empty>','def_goal',0,'p_def_goal_1','multipparser.py',551),
  ('def_goal -> LPAREN COLON GOAL LPAREN AND lista_predicados_p RPAREN RPAREN','def_goal',8,'p_def_goal_2','multipparser.py',554),
  ('def_goal -> LPAREN COLON GOAL LPAREN NOT lista_predicados_p RPAREN RPAREN','def_goal',8,'p_def_goal_5','multipparser.py',558),
  ('def_goal -> LPAREN COLON GOAL COLON AGENT agent_def COLON CONDITION lista_predicados_p RPAREN','def_goal',10,'p_def_goal_3','multipparser.py',562),
  ('def_goal -> LPAREN COLON GOAL RPAREN','def_goal',4,'p_def_goal_4','multipparser.py',566),
  ('lista_predicados_p -> <empty>','lista_predicados_p',0,'p_lista_predicados_p_1','multipparser.py',570),
  ('lista_predicados_p -> LPAREN lista_ids RPAREN lista_predicados_p','lista_predicados_p',4,'p_lista_predicados_p_2','multipparser.py',573),
  ('lista_predicados_p -> LPAREN AND lista_predicados_p RPAREN lista_predicados_p','lista_predicados_p',5,'p_lista_predicados_p_3','multipparser.py',577),
  ('lista_predicados_p -> LPAREN NOT lista_predicados_p RPAREN lista_predicados_p','lista_predicados_p',5,'p_lista_predicados_p_6','multipparser.py',580),
  ('lista_predicados_p -> LPAREN COMP LPAREN lista_ids RPAREN NUM RPAREN lista_predicados_p','lista_predicados_p',8,'p_lista_predicados_p_4','multipparser.py',585),
  ('lista_predicados_p -> LPAREN COMP LPAREN lista_ids RPAREN ID RPAREN lista_predicados_p','lista_predicados_p',8,'p_lista_predicados_p_5','multipparser.py',589),
  ('domain_formalization -> def_domain def_requirements def_types def_constants def_predicates def_functions def_actions','domain_formalization',7,'p_domain_formalization_1','multipparser.py',597),
  ('domain_formalization -> def_domain def_requirements def_types def_predicates def_actions','domain_formalization',5,'p_domain_formalization_2','multipparser.py',602),
  ('domain_formalization -> def_domain def_requirements def_types def_predicates def_functions def_actions','domain_formalization',6,'p_domain_formalization_3','multipparser.py',606),
  ('domain_formalization -> def_domain def_requirements def_types def_constants def_predicates def_actions','domain_formalization',6,'p_domain_formalization_4','multipparser.py',610),
  ('domain_formalization -> def_domain def_requirements def_predicates def_actions','domain_formalization',4,'p_domain_formalization_5','multipparser.py',614),
  ('def_domain -> LPAREN DOMAIN ID RPAREN','def_domain',4,'p_def_domain_1','multipparser.py',618),
  ('def_requirements -> <empty>','def_requirements',0,'p_def_requirements_1','multipparser.py',625),
  ('def_requirements -> LPAREN COLON REQUIREMENTS lista_requirements RPAREN','def_requirements',5,'p_def_requirements_2','multipparser.py',628),
  ('lista_requirements -> <empty>','lista_requirements',0,'p_lista_requirements_1','multipparser.py',633),
  ('lista_requirements -> COLON ID lista_requirements','lista_requirements',3,'p_lista_requirements_2','multipparser.py',637),
  ('def_types -> <empty>','def_types',0,'p_def_types_1','multipparser.py',641),
  ('def_types -> LPAREN COLON TYPES lista_types RPAREN','def_types',5,'p_def_types_2','multipparser.py',644),
  ('def_types -> LPAREN COLON TYPES lista_types MINUS ID RPAREN','def_types',7,'p_def_types_3','multipparser.py',649),
  ('lista_types -> <empty>','lista_types',0,'p_lista_types_1','multipparser.py',653),
  ('lista_types -> ID lista_types','lista_types',2,'p_lista_types_2','multipparser.py',656),
  ('def_constants -> <empty>','def_constants',0,'p_def_constants_1','multipparser.py',661),
  ('def_constants -> LPAREN COLON CONSTANTS lista_constants RPAREN','def_constants',5,'p_def_constants_2','multipparser.py',664),
  ('lista_constants -> <empty>','lista_constants',0,'p_lista_constants_1','multipparser.py',668),
  ('lista_constants -> lista_ids MINUS ID lista_constants','lista_constants',4,'p_lista_constants_2','multipparser.py',672),
  ('def_predicates -> <empty>','def_predicates',0,'p_def_predicates_1','multipparser.py',681),
  ('def_predicates -> LPAREN COLON PREDICATES lista_predicates RPAREN','def_predicates',5,'p_def_predicates_2','multipparser.py',684),
  ('lista_predicates -> <empty>','lista_predicates',0,'p_lista_predicates_1','multipparser.py',691),
  ('lista_predicates -> LPAREN ID p_def RPAREN lista_predicates','lista_predicates',5,'p_lista_predicates_2','multipparser.py',696),
  ('p_def -> lista_var MINUS ID p_def','p_def',4,'p_p_def_1','multipparser.py',717),
  ('p_def -> lista_var','p_def',1,'p_p_def_2','multipparser.py',729),
  ('def_functions -> <empty>','def_functions',0,'p_def_functions_1','multipparser.py',740),
  ('def_functions -> LPAREN COLON FUNCTIONS lista_functions RPAREN','def_functions',5,'p_def_functions_2','multipparser.py',743),
  ('lista_functions -> <empty>','lista_functions',0,'p_lista_functions_1','multipparser.py',746),
  ('lista_functions -> function lista_functions','lista_functions',2,'p_lista_functions_2','multipparser.py',749),
  ('function -> LPAREN ID VAR ID MINUS ID RPAREN','function',7,'p_function_1','multipparser.py',753),
  ('function -> LPAREN ID RPAREN','function',3,'p_function_2','multipparser.py',757),
  ('def_actions -> <empty>','def_actions',0,'p_def_actions_1','multipparser.py',761),
  ('def_actions -> LPAREN COLON ACTION ID a_def RPAREN def_actions','def_actions',7,'p_def_actions_2','multipparser.py',764),
  ('def_actions -> LPAREN COLON ACTION ID COLON AGENT agent_def a_def RPAREN def_actions','def_actions',10,'p_def_actions_3','multipparser.py',771),
  ('agent_def -> ID','agent_def',1,'p_agent_def_1','multipparser.py',776),
  ('agent_def -> VAR ID','agent_def',2,'p_agent_def_2','multipparser.py',780),
  ('agent_def -> VAR ID MINUS ID','agent_def',4,'p_agent_def_3','multipparser.py',784),
  ('a_def -> <empty>','a_def',0,'p_a_def_1','multipparser.py',788),
  ('a_def -> COLON PARAMETERS LPAREN lista_parameters RPAREN COLON PRECONDITION pddl_preconditions COLON EFFECT pddl_effects','a_def',11,'p_a_def_2','multipparser.py',792),
  ('pddl_preconditions -> lista_preds_op','pddl_preconditions',1,'p_pddl_preconditions_1','multipparser.py',797),
  ('pddl_effects -> lista_preds_op','pddl_effects',1,'p_pddl_effects_1','multipparser.py',802),
  ('lista_parameters -> <empty>','lista_parameters',0,'p_lista_parameters_1','multipparser.py',806),
  ('lista_parameters -> VAR ID MINUS ID lista_parameters','lista_parameters',5,'p_lista_parameters_2','multipparser.py',813),
  ('lista_parameters -> lista_var MINUS ID lista_parameters','lista_parameters',4,'p_lista_parameters_3','multipparser.py',829),
  ('lista_parameters -> lista_var','lista_parameters',1,'p_lista_parameters_4','multipparser.py',838),
  ('lista_preds_op -> <empty>','lista_preds_op',0,'p_lista_preds_op_1','multipparser.py',853),
  ('lista_preds_op -> lista_predicados','lista_preds_op',1,'p_lista_preds_op_2','multipparser.py',856),
  ('lista_preds_op -> LPAREN AND lista_preds_op RPAREN lista_preds_op','lista_preds_op',5,'p_lista_preds_op_3','multipparser.py',861),
  ('lista_preds_op -> LPAREN NOT lista_predicados RPAREN','lista_preds_op',4,'p_lista_preds_op_9','multipparser.py',871),
  ('lista_preds_op -> LPAREN FORALL lista_preds_op RPAREN','lista_preds_op',4,'p_lista_preds_op_4','multipparser.py',879),
  ('lista_preds_op -> LPAREN EXISTS lista_preds_op RPAREN','lista_preds_op',4,'p_lista_preds_op_5','multipparser.py',883),
  ('lista_preds_op -> LPAREN IMPLY lista_preds_op RPAREN','lista_preds_op',4,'p_lista_preds_op_6','multipparser.py',887),
  ('lista_preds_op -> LPAREN PREFERENCE [ ID ] RPAREN','lista_preds_op',6,'p_lista_preds_op_7','multipparser.py',891),
  ('lista_preds_op -> LPAREN WHEN lista_preds_op RPAREN','lista_preds_op',4,'p_lista_preds_op_8','multipparser.py',895),
  ('lista_predicados -> LPAREN ID lista_var RPAREN lista_preds_op','lista_predicados',5,'p_lista_predicados_1','multipparser.py',899),
  ('lista_predicados -> LPAREN lista_var MINUS ID RPAREN lista_preds_op','lista_predicados',6,'p_lista_predicados_2','multipparser.py',916),
  ('lista_predicados -> LPAREN COMP lista_var RPAREN lista_preds_op','lista_predicados',5,'p_lista_predicados_3','multipparser.py',920),
  ('lista_predicados -> LPAREN VAR ID COMP ID RPAREN lista_preds_op','lista_predicados',7,'p_lista_predicados_4','multipparser.py',924),
  ('lista_predicados -> LPAREN DECREASE LPAREN ID RPAREN NUM RPAREN','lista_predicados',7,'p_lista_predicados_5','multipparser.py',928),
  ('lista_var -> <empty>','lista_var',0,'p_lista_var_1','multipparser.py',932),
  ('lista_var -> VAR ID lista_var','lista_var',3,'p_lista_var_2','multipparser.py',940),
  ('lista_var -> ID lista_var','lista_var',2,'p_lista_var_3','multipparser.py',947),
  ('lista_ids -> <empty>','lista_ids',0,'p_lista_ids_1','multipparser.py',952),
  ('lista_ids -> ID lista_ids','lista_ids',2,'p_lista_ids_2','multipparser.py',961),
]
