from nova_act import NovaAct
import warnings

warnings.filterwarnings('ignore')

def test_nova_act_simple():
    """Test Nova Act on s-plus-m.ai."""
    
    nova = NovaAct(starting_page="https://www.s-plus-m.ai")
    
    try:
        print("Starting Nova Act...")
        nova.start()
        
        print("Reading page content...")
        response = nova.act("Tell me what are the main points about this company")
        
        print(f"\nResponse: {response}")
        
        return response
    
    except Exception as e:
        print(f"Error: {type(e).__name__}")
        print(f"Message: {str(e)[:300]}")
        return None
    
    finally:
        try:
            nova.stop()
        except:
            pass


if __name__ == "__main__":
    print("=== Testing Nova Act on s-plus-m.ai ===\n")
    result = test_nova_act_simple()
    print("\n=== Test Complete ===")
