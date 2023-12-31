
if ($_SERVER['REQUEST_METHOD'] == 'POST'){
  $name = $_POST['name'];
  $email = $_POST['email'];
  $desc = $_POST['desc'];
        
      
// Connecting to the Database
  $servername = "localhost";
  $username = "root";
  $password = "";
  $database = "contacts";

// Create a connection
  $conn = mysqli_connect($servername, $username, $password, $database);
  // Die if connection was not successful
  if (!$conn){
    die("Sorry we failed to connect: ". mysqli_connect_error());
  }
  else{ 
// Submit these to a database
// Sql query to be executed 
    $sql = "INSERT INTO `contactus` (`name`, `email`, `concern`, `dt`) VALUES ('$name', '$email', '$desc', current_timestamp())";
    $result = mysqli_query($conn, $sql);
 
  if($result){
    echo '<div class="alert alert-success alert-dismissible fade show" role="alert">
    <strong>Success!</strong> Your entry has been submitted successfully!
    <button type="button" class="close" data-dismiss="alert" aria-label="Close">
    <span aria-hidden="true">×</span>
     </button>
     </div>';
  }
  else{
// echo "The record was not inserted successfully because of this error ---> ". mysqli_error($conn);
    echo '<div class="alert alert-danger alert-dismissible fade show" role="alert">
    <strong>Error!</strong> We are facing some technical issue and your entry ws not submitted successfully! We regret the inconvinience caused!
    <button type="button" class="close" data-dismiss="alert" aria-label="Close">
      <span aria-hidden="true">×</span>
      </button>
      </div>';
    }

  }

}

    
?>

<div class="container mt-3">
<h1>Contact us for your concerns</h1>
    <form action="/cwhphp/28_Form.php" method="post">
    <div class="form-group">
        <label for="name">Name</label>
        <input type="text" name="name" class="form-control" id="name" aria-describedby="emailHelp">
    </div>

    <div class="form-group">
        <label for="email">Email</label>
        <input type="email" name="email" class="form-control" id="email" aria-describedby="emailHelp"> 
        <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
    </div>

    <div class="form-group">
        <label for="desc">Description</label>
        <textarea class="form-control" name="desc" id="desc" cols="30" rows="10"></textarea> 
    </div>
    
    <button type="submit" class="btn btn-primary">Submit</button>
    </form>
</div>