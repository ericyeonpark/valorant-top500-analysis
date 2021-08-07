from sklearn.linear_model import Ridge
import data_wrangle as dw



# Ridge Regression Model
model = make_pipeline(OneHotEncoder(use_cat_names=True),
                      SimpleImputer(strategy = 'mean'),
                      StandardScaler(),
                      Ridge(alpha = 100),
                      )
                                             
model.fit(X_train, y_train)