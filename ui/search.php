<?php
	if (isset($_GET["search_item"]))
	{
		$search_item = strtolower($_GET["search_item"]);
	}
	else {
		header("Location: index.html");
	}
	$data = json_decode(file_get_contents("js/data.txt"), false);
	$search_data = "";
	foreach ($data as $var) {
		if (substr_count(strtolower($var -> author), $search_item) > 0)
		{
			if ($var -> abstract == "")
			{
				$var -> abstract = "No Publication Abstract Provided By The Author";
			}
			$search_data .= '<div class="col-md-12">
                  <a href="'.$var -> research_link.'" class="blog-entry element-animate" data-animate-effect="fadeIn">
                    <h2>'.$var -> research_title.'</h2>
                    <p>'.$var -> abstract.'</p>
                    <div class="blog-content-body">
                      <div class="post-meta">
                        <span class="author mr-2"><img src="images/person_1.jpg" alt="Author"> '.$var -> author.'</span>
                      </div>
                    </div>
                  </a>
                </div>';
		}
	}
	if ($search_data == ""){
		$search_data = "<h1>No results found for your query</h1>";
	}
?>

<!doctype html>
<html lang="en">
  <head>
    <title>X-Crawler - Research Publication Watchlist</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <link href="https://fonts.googleapis.com/css?family=Josefin+Sans:300, 400,700|Inconsolata:400,700" rel="stylesheet">

	<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.1/css/all.css" integrity="sha384-50oBUHEmvpQ+1lW4y57PTFmhCaXp0ML5d60M1M7uH2+nqUivzIebhndOJK28anvf" crossorigin="anonymous">

	<link rel="shortcut icon" href="images/logo.png" type="image/x-icon">

    <link rel="stylesheet" href="css/bootstrap.css">
    <link rel="stylesheet" href="css/animate.css">
    <link rel="stylesheet" href="css/owl.carousel.min.css">

    <!-- Theme Style -->
    <link rel="stylesheet" href="css/style.css">
  </head>
  <body>


    <div class="wrap">

      <header role="banner">
        <div class="top-bar">
          <div class="container">
            <div class="row">
              <div class="col-9 social">
                <a href="https://github.com/LordGhostX/X-Crawler"><span class="fab fa-github"></span></a>
              </div>
              <div class="col-3 search-top">
                <!-- <a href="#"><span class="fa fa-search"></span></a> -->
                <form action="search.php" class="search-top-form">
                  <span class="icon fa fa-search"></span>
                  <input type="text" id="s" placeholder="Enter Author or Title to search..." name="search_item">
                </form>
              </div>
            </div>
          </div>
        </div>

        <div class="container logo-wrap">
          <div class="row pt-5">
            <div class="col-12 text-center">
              <a class="absolute-toggle d-block d-md-none" data-toggle="collapse" href="#navbarMenu" role="button" aria-expanded="false" aria-controls="navbarMenu"><span class="burger-lines"></span></a>
              <h1 class="site-logo"><a href="index.html"><img src="images/logo.png"> X-Crawler</a></h1>
			   <h2>Research Publication Watchlist</h2>
            </div>
          </div>
        </div>

        <nav class="navbar navbar-expand-md  navbar-light bg-light">
          <div class="container">


            <div class="collapse navbar-collapse" id="navbarMenu">
              <ul class="navbar-nav mx-auto">
                <li class="nav-item">
                  <a class="nav-link active" href="index.html">Home</a>
                </li>

                <li class="nav-item">
                  <a class="nav-link" href="about.html">About</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" href="contact.html">Contact</a>
                </li>
              </ul>

            </div>
          </div>
        </nav>
      </header>
      <!-- END header -->

      <section class="site-section py-sm">
        <div class="container">
          <div class="row">
            <div class="col-md-6">
              <h4 class="mb-4" id="homee">Search results for "<?php echo $search_item; ?>"</h4>
            </div>
          </div>
          <div class="row blog-entries">
            <div class="col-md-12 col-lg-12 main-content">
              <div class="row">
                <?php echo $search_data; ?>
              </div>
            </div>

            <!-- END main-content -->

            
          </div>
        </div>
      </section>
	   <center><a href="#homee"><button style="border: none; border-radius: 50%;"><i class="fas fa-chevron-circle-up" style="background: #fff; text-align: left; border: none; border-radius: 50%; padding: 30px;"></i></button></a></center> <br>
      <footer class="site-footer">
        <div class="container">
          <div class="row">
            <div class="col-md-12 text-center">
              <p class="small">
            <!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. -->
            X-Crawler | This template is made with <i class="fa fa-heart text-danger" aria-hidden="true"></i> by <a href="https://colorlib.com" target="_blank" >Colorlib</a>
            <!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. -->
            </p>
            </div>
          </div>
        </div>
      </footer>
      <!-- END footer -->

    </div>

    <!-- loader -->
    <div id="loader" class="show fullscreen"><svg class="circular" width="48px" height="48px"><circle class="path-bg" cx="24" cy="24" r="22" fill="none" stroke-width="4" stroke="#eeeeee"/><circle class="path" cx="24" cy="24" r="22" fill="none" stroke-width="4" stroke-miterlimit="10" stroke="#f4b214"/></svg></div>

    <script src="js/jquery-3.2.1.min.js"></script>
    <script src="js/jquery-migrate-3.0.0.js"></script>
    <script src="js/popper.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <script src="js/owl.carousel.min.js"></script>
    <script src="js/jquery.waypoints.min.js"></script>
    <script src="js/jquery.stellar.min.js"></script>


    <script src="js/main.js"></script>
  </body>
</html>
