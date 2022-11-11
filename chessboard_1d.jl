using Plots


N_PERSON = 100
N_ITERATIONS = 50
MIN_CONCENTRATION_INITIAL = 1
MAX_CONCENTRATION_INITIAL = 5
PRODUCTION_RATE = 5
# Critical value for this parameter is < 1.0
DEGRADATION_RATE = 0.2


function add_inverse_neighbors!(a::Vector{Float64})
    da = PRODUCTION_RATE ./ (circshift(a, 1) + circshift(a, -1))
    da -= DEGRADATION_RATE * a
    a += da
    return a
end


function main()
    a::Vector{Float64} = rand(MIN_CONCENTRATION_INITIAL:MAX_CONCENTRATION_INITIAL, N_PERSON)
    
    results = zeros(N_ITERATIONS+1, N_PERSON)
    results[1,:] = a

    for i in 1:N_ITERATIONS+1
        a = add_inverse_neighbors!(a)
        results[i,:] = a
    end

    display(results)

    p = plot(results)
    savefig(p, "chessboard_1d.png")
end

main()
