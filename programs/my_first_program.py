from nada_dsl import *
import telemetry  # Hypothetical telemetry library

# Enable telemetry with a unique identifier for this instance
telemetry_id = "big-program-instance-id-67890"
telemetry.enable(telemetry_id)

def nada_main():
    # Define parties
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")

    # Inputs from Party1
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Inputs from Party2
    my_int3 = SecretInteger(Input(name="my_int3", party=party2))
    my_int4 = SecretInteger(Input(name="my_int4", party=party2))

    # Log the inputs for telemetry purposes
    telemetry.log("Input my_int1 from Party1", my_int1)
    telemetry.log("Input my_int2 from Party1", my_int2)
    telemetry.log("Input my_int3 from Party2", my_int3)
    telemetry.log("Input my_int4 from Party2", my_int4)

    # Perform computations
    sum_result = my_int1 + my_int2
    telemetry.log("Sum result of my_int1 and my_int2", sum_result)

    product_result = my_int3 * my_int4
    telemetry.log("Product result of my_int3 and my_int4", product_result)

    if my_int2 != 0:
        division_result = my_int1 / my_int2
    else:
        division_result = 0  # Handle division by zero
    telemetry.log("Division result of my_int1 by my_int2", division_result)

    combined_result = sum_result + product_result - division_result
    telemetry.log("Combined result of all operations", combined_result)

    # Outputs
    return [
        Output(sum_result, "sum_output", party1),
        Output(product_result, "product_output", party2),
        Output(division_result, "division_output", party1),
        Output(combined_result, "combined_output", party1)
    ]

# Start the main function
if _name_ == "_main_":
    nada_main()