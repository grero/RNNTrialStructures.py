import juliacall
from array import array
jl = juliacall.newmodule("RNNTrialStructs")
jl.seval("using RNNTrialStructures")

def get_navigation_trialstruct(min_n_steps, max_n_steps, inputs, outputs):
    arena = jl.RNNTrialStructures.MazeArena()
    angles = jl.convert(jl.Vector[jl.Float32], jl.collect(jl.range(jl.Float32(0), stop=jl.Float32(2*jl.pi), length=16)))
    apref = jl.RNNTrialStructures.AngularPreference(angles, jl.convert(jl.Float32,5), jl.Float32(0.8))
    inputs = jl.Vector[jl.Symbol]([jl.Symbol(ip) for ip in inputs])
    outputs = jl.Vector[jl.Symbol]([jl.Symbol(ip) for ip in outputs])
    trialstruct = jl.RNNTrialStructures.NavigationTrial(min_n_steps, max_n_steps, inputs, outputs, arena, apref)

    return trialstruct

def get_batch_generator(trialstruct, ntrials,fov=jl.pi/3, head_direction_step=jl.pi/3, p_stay=1/3, p_hd=0.8,dt=20.0):
    ntrials = jl.convert(jl.Int64, ntrials)
    trial_generator = jl.RNNTrialStructures.generate_trials(trialstruct, ntrials, dt, fov=fov,hd_step=head_direction_step, p_stay=p_stay, p_hd=p_hd) 
    return trial_generator

