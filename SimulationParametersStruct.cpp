/*
 * SimulationParametersStruct.cpp
 *
 *  Created on: Mar 13, 2015
 *      Author: Mark Wittekind and Drew Murray
 */
#ifndef SIM_PARAMS_UNIQUE
#define SIM_PARAMS_UNIQUE

struct SimulationParameters
{
	const unsigned short WIDTH = 200;
	const unsigned short HEIGHT = 200;
	unsigned short MAXTIME = 3000;
	float TIMESTEP = 1;
	unsigned int MAXTIMESTEPS = short(MAXTIME/TIMESTEP);
	float COUPLING_CONSTANT = 1;
	float temperature = 2;
	float BOLTZMAN_CONSTANT = 1;
	unsigned int PRINT_FREQ = 50000;
	float MIN_TEMP = 1;
	float MAX_TEMP = 5;
	float TEMP_STEP = .002;
	bool CRIT_MODE = false;
	unsigned short CRIT_REPEATS = 10;
	bool var_timestep = true;

	//TODO magnetization vs temp
	// T critical
	// Susceptibility (d<m>/dT)
	// Internal Energy
	// Heat capacity (dE/dT)
	// Critical exponents:
	// 		log(X) vs log(T)
	// 		log(mag) vs log(T)
};

#endif

